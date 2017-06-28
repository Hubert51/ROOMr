from app import app, db, lm, oid
from flask import render_template, flash, redirect, session, url_for, request, g
from flask_login import login_user, logout_user, current_user, login_required
from .forms import LoginForm
from .models import User

def getInfo(info):
	state = info[-1]
	roomInfo = info[0:-1]
	for i in range(len(roomInfo)):
		# this is situation that we have room number and section number
		if ( roomInfo[i].isalpha() ):
			roomNum = roomInfo[0:i]
			roomSection = roomInfo[i:]
			return (state, roomNum, roomSection)
		# this is the situation that we only have room number
		if (i==(len(roomInfo)-1)) :
			return state, roomInfo 
			
@app.route("/<info>")
def update(info):
	myTuple = getInfo(info)
	if len(myTuple)==2:
		state, roomNum = myTuple
	else:
		state, roomNum, roomSection = getInfo(info)

	return roomNum

@app.route("/main")
def roomr():
	return render_template('main.html')

@app.before_request
def befor_request():
	g.user = current_user

@app.route('/login', methods=['GET', 'POST'])
@oid.loginhandler
def login():
	if g.user is not None and g.user.is_authenticated:
		return redirect(url_for('index'))

	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' %
			  (form.openid.data, str(form.remember_me.data)))
		session['remember_me'] = form.remember_me.data
		return oid.try_login(form.openid.data, ask_for = ['nickname', 'email'])
		# return redirect('/index')
	return render_template('login.html', 
						   title='Sign In',
						   form=form,
						   providers = app.config['OPENID_PROVIDERS'])

@oid.after_login
def after_login(resp):
	if resp.email is None or resp.email == "":
		flash('Invalid login. Please try again.')
		return redirect(url_for('login'))
	user = User.query.filter_by(email=resp.email).first()
	if user is None:
		nickname = resp.nickname
		if nickname is None or nickname == "":
			nickname = resp.email.split('@')[0]
		user = User(nickname = nickname, email=resp.email)
		db.session.add(user)
		db.session.commit()
	remember_me = False
	if 'remember_me' in session:
		remember_me = session['remember_me']
		session.pop('remember_me' , None)
	login_user(user, remember = remember_me)
	return redirect(request.args.get('next') or url_for('index'))


@app.route('/')
@app.route('/index')
@login_required
def index():

	user = g.user
	posts = [  # fake array of posts
		{ 
			'author': {'nickname': 'John'}, 
			'body': 'Beautiful day in Portland!' 
		},
		{ 
			'author': {'nickname': 'Susan'}, 
			'body': 'The Avengers movie was so cool!' 
		}
	]
	return render_template("index.html",
						   title='Home',
						   user=user,
						   posts=posts)

@lm.user_loader
def load_user(id):
	return User.query.get(int(id))	# we need to change the type of id. Since it is unicode in flask login.
									# we need to int type

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))




















