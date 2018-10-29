from flask import Flask, render_template, request
import random
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"
    
@app.route("/html_tag")
def html_tag():
    return "<h1>Hello flask!!!</h1>"
    
@app.route("/long_html")
def long_html():
    return """
    <h1>여러줄로 보내봅시다.</h1>
    <ul>
        <li>첫번째</li>
        <li>두번째</li>
        <li>세번째</li>
    </ul>
    """
    
@app.route("/html_file")
def html_file():
    return render_template("html_file.html")
    
@app.route("/hello/<string:name>")
def hello(name):
    return render_template("hello_people.html", people_name = name)
    
@app.route("/cube/<int:num>")
def cube(num):
    # num = num**3
    return render_template("cube.html",num = num)
    # 두가지 방법 1. app.py에서 연산해서 넘기기 2. html파일에서 연산하기

@app.route("/lunch")
def lunch():
    lunch_menu = ["20층", "김밥카페"]
    pick = random.choice(lunch_menu)
    return render_template("lunch.html", pick=pick, menu=lunch_menu) 

@app.route("/lotto")
def lotto():
    lotto_nums = list(range(1,46))
    lucky = random.sample(lotto_nums,6)
    return render_template("lotto.html",lucky_num = sorted(lucky))
    
@app.route("/naver")
def naver():
    return render_template("naver.html")
    
@app.route("/opgg")
def opgg():
    return render_template("opgg.html")
    
    
# pip install bs4 requests
@app.route("/summoner")
def summoner():
    userName = request.args.get('userName')
    url = "http://www.op.gg/summoner/userName="
    req = requests.get(url+userName)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    
    win = soup.select(
    '#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins'
    )
    
    if len(win) == 0:
        return render_template("summoner.html" ,win = "랭겜 안함")
        
    lose = soup.select(
    '#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses'
    )[0].text
    game_result = soup.select('.GameResult')
    for game in game_result:
        print(game.text.strip())
    
    f = open("list.txt", 'a+')
    for i in range(1, 11):
        data = "hihi"
        f.write(data)
    f.close()
    
    
    import csv
    import datetime

    f = open('output.csv', 'a+', encoding='utf-8', newline='')
    wr = csv.writer(f)
    wr.writerow([win,lose,datetime.datetime.now()])
    f.close()
    
    return render_template("summoner.html" ,win = win, lose = lose)
    
    
@app.route('/rank')
def rank():
    import csv
 
    f = open('output.csv', 'r', encoding='utf-8')
    rank = csv.reader(f)
    # for line in rank:
    #     print(line)
    # # f.close()    
    
    return render_template("rank.html", rank = rank)