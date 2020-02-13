from bs4 import BeautifulSoup
import webbrowser
import requests
import time

from balloontip import WindowsBalloonTip, balloon_tip

if __name__ == "__main__":
    _name = "김회민"
    _first_start = True

    _lists = [ ['','','','','','','',''] for _ in range(23) ]

    try:
        while True:
            html = requests.get('http://iwork.hrcglobal.com/')
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
                    balloon_tip('{}님 환영합니다!!'.format(_name), '오늘 하루도 즐거운 하루 되세요.')
                    _first_start = False
                else:
                    balloon_tip('새로운 업무가 업데이트되었습니다.', '홈페이지를 확인해주세요.')
                
                url = 'http://iwork.hrcglobal.com/'
                webbrowser.open(url)
            time.sleep(10)
    except KeyboardInterrupt:
        pass