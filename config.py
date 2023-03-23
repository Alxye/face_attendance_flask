# 安装mysql5.6 8.x    安装界面化操作工具Navicate Heidsql 
# 1、pip install pymysql
# 2、pip install Flask-SQLAlchemy


# --------------------配置数据库---------------------
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)


appID = 'wxc244d47cebbff649'  # 开发者关于微信小程序的appID
appSecret = 'b643fa0da74a0eb473bc6b16b4924902'  # 开发者关于微信小程序的appSecret
template_id = "7hzQP9xi-rCy5dwWIUn-SS4OKyZgUceRS6FelBDku34"

HostName = "101.132.152.202"
Port = 3306  # 默认为3306，需要自行修改
UserName = "root"  # 默认用户名
Password = "Admin_10081zxx"
DataBase = "wechat"

# 数据库配置                                               用户名：密码@ip：port/数据库名字
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@101.132.152.202:3306/wechat'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Admin_10081zxx@localhost:3306/wechat'
app.config['SQLALCHEMY_ECHO'] = True
# 数据库操作对象
db_init = SQLAlchemy(app)

SECRET_KEY = "attendance_management_system"



# app = Flask(__name__)
# 数据库配置                                               用户名：密码@ip：port/数据库名字
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Test123@!@127.0.0.1:3306/garbage'
# CORS(app, resources=r'/*')
#
# user = 'root'
# password = parse.quote_plus('123456')
# database = 'wechat'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://%s:%s@101.132.152.202:3306/%s' % (user, password, database)
#
# # 数据库操作对象
# db = SQLAlchemy(app)
