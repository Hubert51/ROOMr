#encoding:utf-8

import os


WTF_CSRF_ENABLED = True	
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
	{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
	{'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
	{'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
	{'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
	{'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI='mysql://root:gengruijie@localhost:3306/test_roomr' #这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建的数据库名text1
SQLALCHEMY_TRACK_MODIFICATIONS = True

SQLALCHEMY_COMMIT_ON_TEARDOWN=True #设置这一项是每次请求结束后都会自动提交数据库中的变动
# db = SQLAlchemy(app)

