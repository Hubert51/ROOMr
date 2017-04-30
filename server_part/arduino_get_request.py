import urllib2

# http://gengruijie.pythonanywhere.com is my homepage

# if the detector finds that there is peope in the room. The state will be has people,
# then the get request sent by arduino will be 551c0. 551c is the room number. The "1"
# is the state of the room which shows having people. Then the backend will change the  
# database according to the URL. 
if state=="has people":
	response = urllib2.urlopen('http://gengruijie.pythonanywhere.com/551c1')

elif state == "empty": 
	response = urllib2.urlopen('http://gengruijie.pythonanywhere.com/551c0')
html = response.read()