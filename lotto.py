import requests
from bs4 import BeautifulSoup
import random

req = requests.get("https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo=837").text
soup = BeautifulSoup(req, 'html.parser')
for i in range(6):
    lucky = soup.select_one(".ball_645").text
    print(lucky)


#article > div:nth-child(2) > div > div.win_result > div > div.num.win

#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span.ball_645.lrg.ball1
#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span:nth-child(2)
#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span:nth-child(3)
#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span:nth-child(4)
#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span.ball_645.lrg.ball4
#article > div:nth-child(2) > div > div.win_result > div > div.num.win > p > span.ball_645.lrg.ball5

#article > div:nth-child(2) > div > div.win_result > div > div.num.bonus > p > span