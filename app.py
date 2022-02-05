from flask import Flask,render_template
import sqlite3
app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html")

@app.route('/index')
def index():  # put application's code here
    return render_template("index.html")   #等同于返回 home（）

@app.route('/movie')
def movie():
    datalist=[]
    con=sqlite3.connect("move.db")
    cur=con.cursor()
    sql="select * from movie250"
    data=cur.execute(sql)
    for item in data:
        datalist.append(item)
    cur.close()
    con.close()
    print(datalist)
    return render_template("movie.html",movies=datalist)

@app.route('/score')
def score():  # put application's code here
    score = []   #因为数据库关闭之后就不能用立马的数据了，所以要及时保存
    num=[]
    con = sqlite3.connect("move.db")
    cur = con.cursor()
    sql = "select score,count(score) from movie250 group by score" #采用分组函数进行分组
    data = cur.execute(sql)
    for item in data:
        score.append(item[0])
        num.append(item[1])
    cur.close()
    con.close()
    return render_template("score.html",score=score,num=num)

@app.route('/word')
def word():  # put application's code here
    return render_template("word.html")

@app.route('/team')
def team():  # put application's code here
    return render_template("team.html")

if __name__ == '__main__':
    app.run()
