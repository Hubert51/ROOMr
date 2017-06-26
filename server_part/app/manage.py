
from flask import Flask
from flask import render_template
import MySQLdb

import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


app = Flask(__name__)
# This is online version of database
# db = MySQLdb.connect(host="Gengruijie.mysql.pythonanywhere-services.com",user="Gengruijie",passwd="jixiaofang123",db="Gengruijie$ROOMr")

# this is local database for testing and developing
db = MySQLdb.connect(host="127.0.0.1",user="root",passwd="gengruijie",db="ROOMR")
cur = db.cursor()

def getInfo(info):
    state = info[-1]
    roomInfo = info[0:-1]
    for i in range(len(roomInfo)):
        if ( roomInfo[i].isalpha() ):
            roomNum = roomInfo[0:i]
            roomSection = roomInfo[i:]
    return (state, roomNum, roomSection)


@app.route('/')
def hello_world():
    query551 = "select state from Info WHERE num = 551"
    cur.execute(query551)
    state551 = cur.fetchone()
    print(state551)

    state = state551[0]
    if(state551[0] == 1 ):
        state1 = "Occupied"
    else :
        state1 = "empty"
    return render_template("main.html")#,state = state1)

@app.route("/<info>")
def update(info):
    state, roomNum, roomSection = getInfo(info)
            
    return roomNum
    # query = "UPDATE Info SET state = 0  WHERE num=551 "
    # cur.execute(query)
    # db.commit()
    # return "succeed"

@app.route("/551c1")
def dominate():
    query = "UPDATE Info SET state = 1  WHERE num=551 "
    cur.execute(query)
    db.commit()
    return "dominate"

if __name__ == '__main__':
    app.run(debug=True);



