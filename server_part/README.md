# ROOMr server 

## Introduction 

Server part is developed by python frame flask and MySQL database. The backend is divided into two parts.
First part is communication between detector and server. Raspberry Pi will send get request. The server 
will determine the inforamtion in the URL to determine whether the room has people or not.
  ```python
  if state=="has people":
   response = urllib2.urlopen('http://gengruijie.pythonanywhere.com/551c1')

  elif state == "empty": 
   response = urllib2.urlopen('http://gengruijie.pythonanywhere.com/551c0')
  ```
<br>
The '0' means no people in the room, the 1 means the room is occupied.
Different arduino has different URL. So the backend can use URL to determine the source of the data.
The server use mysql python to updata into the database.
  ```python
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
  ```
Second part is users and server. The users will just see our homepage. the state will tell them 
whether the room is occupied or not. Every time, they request the website. The backend will cehck the 
databse of every room states. So they can know which one is empty or not.
 ![image](https://github.com/Hubert51/ROOMr/blob/master/server_part/readme_picture/homepage.png)


Built With
1. Flask - A micro web framework for python.
2. MySQL - A SQL type database
