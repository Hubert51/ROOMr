from app import db

class Room(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	roomNo = db.Column(db.Integer)
	roomSection = db.Column(db.String(64))
	location = db.Column(db.String(120))
	state = db.Column(db.Integer)

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonmymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self,id)		#python 2
		except NameError:	
			return str(self,id)			#python 3

	def __repr__(self):
		return 'The state of room %r is %r' %(self.roomNo, state)

class User(db.Model):
	"""docstring for User"""
	id = db.Column(db.Integer, primary_key=True)
	nickname = db.Column(db.String(64),index=True, unique=True)
	email = db.Column(db.String(120), index= True, unique=True)

	@property
	def is_authenticated(self):
		return True

	@property
	def is_active(self):
		return True

	@property
	def is_anonmymous(self):
		return False

	def get_id(self):
		try:
			return unicode(self.id)		#python 2
		except NameError:	
			return str(self.id)			#python 3


	def __repr__(self):
		return '<User %r>' % (self.nickname)







		