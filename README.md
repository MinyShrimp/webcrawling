# 회사용 업무 웹사이트 자동 크롤링 제작

## 왜 만들었어요?
우리 회사에서는 인턴에게(나에게) 업무를 요청할 때 다른 사람들이랑 겹치지 않게 하도록 웹사이트를 만들어 관리하도록 하고 있었다. 그래서 나는 이 웹사이트를 주기적으로 새로고침하여 업무가 있는지 확인을 해야했다. (물론 메일이 와야 진행이 가능하지만)

나는 이 과정이 귀찮게 느껴져 python을 이용해 웹크롤링을 하기로 결정했다. 

개발 목표는 아래 3가지로, 간단한 프로그램이다.
>1. 일정 주기마다 사이트를 새로고침해서 코드를 가져온다.
>2. 만약, 변한게 있다면 윈도우 메세지로 표시하게 해준다.

## Request와 BeautifulSoup 설치
설치
```
pip install bs4
pip install requests
```
코드
```python
## main.py ##
from bs4 import BeautifulSoup
import requests
```
우선, 나는 **requests**와 **BeautifulSoup**를 사용할 것이다. 

위와 같이 작성 후에 실행했는데 아무것도 뜨지 않는다면 OK다. 
>이번엔 **selenium**을 사용하지 않을 것인데, 
>
>이유는 크롤링해오는 웹사이트 자체가 ajax로 불러오는게 없고 고정되어있기 때문에, 그냥 일정 주기마다 **requests.get** 하면 모든 정보가 불러와지기 때문이다. 
>
>만약, 당신이 개발해야되는 환경이 무언가를 불러오는 동적 웹사이트인 경우 **selenium** 쓰는게 편하다.

<<<<<<< HEAD
=======


>>>>>>> 6d0211851cea1cfdffd895b031e1dffb2fa343a2
## 웹사이트 접속
우선, 크롤링하고 싶은 웹사이트에 접속해서 F12(Chrome)를 눌러 html을 확인해보자. Elements 탭에서 확인이 가능하다.

html코드를 처음 본 사람들은 이게 뭔가 싶을거다. html 구성을 제대로 알고 있다면 더 좋겠지만, 지금은 무시해도 좋다. 

침착하게 **Ctrl + Shift + C**를 눌러보자. 그럼 신기하게도 내 마우스를 따라서 구성품들의 정보를 알려줄 것이다. 정보를 알고 싶은 곳에 가서 클릭해보자.

그럼, Elements 탭에서 그 구성품의 위치를 활성화시켜주는데 그 부분을 마우스 오른쪽 클릭을 하고 **Copy > Copy selector**를 클릭하자. 그러면, 현재 클립보드에 구성품의 위치가 저장됐을 것이다.

그것을 아래와 같이 입력하자.
```python
html = requests.get('http://') # 당신의 url
soup = BeautifulSoup(html.content, 'html.parser')
trs  = soup.select('') # ''안에 붙여넣기
```
나의 경우에는 table의 td안에 가져오고 싶은 정보가 있어서, table의 tr을 가져와서 배열로 저장했다.
```python
trs  = soup.select('#body > section > table:nth-child(4) > tr')
```

<<<<<<< HEAD
=======



>>>>>>> 6d0211851cea1cfdffd895b031e1dffb2fa343a2
## 크롤링
먼저, 데이터 비교를 위한 2중 배열을 선언한다. 처음엔 아예 빈 문자열로 채워서 무조건 다르게 만들어 준다.

나의 경우, 가로 8칸, 새로 23칸이 필요하여 아래와 같이 선언해주었다.
``` python
_lists = [ ['','','','','','','',''] for _ in range(23) ]
```
이후, 웹사이트와 비교해서 다른지 확인해야하는데, 나는 아래와 같이 작성했다.
```python
try:
    for i, r in enumerate(trs):
        # #body > section > table:nth-child(4) > tr > td
        tds = r.select('td') 
        for j, d in enumerate(tds):
            # 비교해서 하나라도 다르면,
            if _lists[i][j] != d.text.strip():
                # 강제 예외 발생
                raise EOFError
except EOFError:
    ## 만약 하나라도 다르면,
    for i, r in enumerate(trs):
        tds = r.select('td')
        for j, d in enumerate(tds):
            # _lists 업데이트
            _lists[i][j] = d.text.strip()
    ## 윈도우 메세지 출력
    # 하지만 지금은 일단 테스트용으로 출력만 해보자.
    print(_list)
```
위의 코드에서 하나라도 다르면 **EOFError**를 강제로 일으켜 적용해주었는데, 실제 환경에서 이러면 맞을 수도 있으니 조심하자. *(만약에 저렇게 코드를 짰는데 실제로 **EOFError**가 났다면 그 오류를 발견하는데 더욱 힘들어질 수 있다.)* 

어차피 나는 개인적으로 만들었고, **EOFError**가 발생할 여지도 없어서 사용했지만, 실제 환경에서는 모르는 일이다. 

위와 같이 입력하고 실행해보자. **_list** 변수에 정보가 담겨있다면 성공이다.


## 윈도우 메세지 출력
이는 구글에서 python balloon tip 이라 쳤더니 나온 git 사이트에서 가져왔다.

><https://gist.github.com/BoppreH/4000505>

위의 사이트에 접속해서 코드를 긁어와서 같은 폴더에 `balloontip.py` 라는 이름으로 저장하자.

그 후, `main.py` 맨 위에 아래 코드를 작성한다.
```python
from balloontip import balloon_tip
```
그리고 위에서 임시로 출력했던 `print(_list)` 를 지우고 다음과 같이 입력한다.
```python
## 윈도우 메세지 출력
#print(_list)
balloon_tip('새로운 업무가 업데이트되었습니다.', '홈페이지를 확인해주세요.')
```
여기까지 입력하고 실행했을때, 윈도우 메세지가 나왔다면 성공이다.


## 일정 주기마다 새로고침을 해보자
위의 모든 과정이 성공적으로 진행되었다면, 이제 무한 루프를 돌면서 일정 주기마자 위의 코드를 반복해주면 된다. 

이는 매우 간단하게 해결이 가능한데, while을 둘러주면 된다.
```python
while True:
    html = requests.get('http://iwork.hrcglobal.com/')
    soup = BeautifulSoup(html.content, 'html.parser')
    trs = soup.select('#body > section > table:nth-child(4) > tr')
    try:
        for i, r in enumerate(trs):
            tds = r.select('td')
        for j, d in enumerate(tds):
            if _lists[i][j] != d.text.strip():
                raise EOFError
    except EOFError:
        for i, r in enumerate(trs):
            tds = r.select('td')
            for j, d in enumerate(tds):
                _lists[i][j] = d.text.strip()
        balloon_tip('새로운 업무가 업데이트되었습니다.', '홈페이지를 확인해주세요.')
```
그런데, 이러면 새로고침이 1 tick마다 진행이 되는데, 잘못했다가는 과부하가 올 수도 있으니까 조금 텀을 줘야한다.

텀을 주는 방법또한 간단하다. 맨 위에 아래의 코드를 입력해주고,
```python
import time
```
while문 끝에 다음 코드를 입력해주면 된다.
```python
time.sleep(10) # 10초 동안 프로그램을 '멈춘다'
```
이제, 당신의 코드는 10초마다 루프를 한번씩 돌게 될것이다.


## 프로그램 종료하기
하지만, 위와 같이 무턱대고 무한루프를 돌리게되면 정상적인 종료가 힘들어질 것이다.

이는 예상치 못하는 결과를 초래할 수도 있기 때문에 다음과 같은 코드를 입력해준다.
```python
try:
    while True:
        html = requests.get('http://iwork.hrcglobal.com/')
        soup = BeautifulSoup(html.content, 'html.parser')
        trs = soup.select('#body > section > table:nth-child(4) > tr')
        try:
            for i, r in enumerate(trs):
                tds = r.select('td')
            for j, d in enumerate(tds):
                if _lists[i][j] != d.text.strip():
                    raise EOFError
        except EOFError:
            for i, r in enumerate(trs):
                tds = r.select('td')
                for j, d in enumerate(tds):
                    _lists[i][j] = d.text.strip()
            balloon_tip('새로운 업무가 업데이트되었습니다.', '홈페이지를 확인해주세요.')
        time.sleep(10)
except KeyboardInterrupt:
    # release 코드
    pass
```
**KeyboardInterrupt** 예외는 프로그램 실행 중에 'Ctrl+C'나 'Delete'키를 누르게 되면 발생되는 예외로, time.sleep 중에도 키를 누르면 프로그램이 꺼지게 된다.

만약, 당신이 release가 필요한 코드를 입력했다면, pass를 지우고 그 블럭에 입력하면 된다.


## 웹페이지 띄우기
이제 마지막으로 윈도우 메세지가 뜸과 동시에 내용을 확인하기 위해 해당 웹페이지를 직접 띄워주는 코드를 입력한다. 먼저, 아래와 같은 코드를 `main.py` 맨위에 입력해주도록 하자.
```python
import webbrowser
```
webbrowser는 기본 포함된 파일이기 때문에 따로 설치할 필요는 없다.
```python
#...
except EOFError:
    for i, r in enumerate(trs):
        tds = r.select('td')
        for j, d in enumerate(tds):
            _lists[i][j] = d.text.strip()

    balloon_tip('새로운 업무가 업데이트되었습니다.', '홈페이지를 확인해주세요.')
    ## 추가
    url = 'http://' # 당신의 url
    webbrowser.open(url)
#...
```
이제 알람이 올때 마다 당신이 설정해둔 기본 웹브라이저에 웹사이트가 자동으로 띄워질 것이다.


## 끝내며
마지막으로 전체 코드를 보여주고 글을 마치겠다.
```python
from bs4 import BeautifulSoup
import webbrowser
import requests
import time

from balloontip import balloon_tip

if __name__ == "__main__":
    _name = "새우" # 당신의 이름
    _first_start = True

    _lists = [ ['','','','','','','',''] for _ in range(23) ]

    try:
        while True:
            html = requests.get('http://')  # 당신의 url
            soup = BeautifulSoup(html.content, 'html.parser')
            trs  = soup.select('#body > section > table:nth-child(4) > tr')
            try:
                for i, r in enumerate(trs):
                    tds = r.select('td')
                    for j, d in enumerate(tds):
                        if _lists[i][j] != d.text.strip():
                            raise EOFError
            except EOFError:
                for i, r in enumerate(trs):
                    tds = r.select('td')
                    for j, d in enumerate(tds):
                        _lists[i][j] = d.text.strip()
                
                if _first_start:
                    balloon_tip('{}님 환영합니다!!'.format(_name), \
                        '오늘 하루도 즐거운 하루 되세요.')
                else:
                    balloon_tip('새로운 업무가 업데이트되었습니다.', \
                        '홈페이지를 확인해주세요.')
                
                url = 'http://' # 당신의 url
                webbrowser.open(url)
            time.sleep(10)
    except KeyboardInterrupt:
        pass
```
