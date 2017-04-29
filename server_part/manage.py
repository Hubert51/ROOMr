# A very simple Flask Hello World app for you to get started with...

from flask import Flask
from flask import render_template
import MySQLdb


app = Flask(__name__)
db = MySQLdb.connect(host="Gengruijie.mysql.pythonanywhere-services.com",user="Gengruijie",passwd="jixiaofang123",db="Gengruijie$ROOMr")
cur = db.cursor()


@app.route('/')
def hello_world():
    query551 = "select state from Info WHERE num = 551"
    cur.execute(query551)
    state551 = cur.fetchone()

    # state = state551[0]
    if(state551[0] == 1 ):
        state1 = "Occupied"
    else :
        state1 = "empty"
    return render_template("table.html",state = state1)

@app.route("/551c0")
def succeed():
    query = "UPDATE Info SET state = 0  WHERE num=551 "
    cur.execute(query)
    db.commit()
    return "succeed"

@app.route("/551c1")
def dominate():
    query = "UPDATE Info SET state = 1  WHERE num=551 "
    cur.execute(query)
    db.commit()
    return "dominate"



