from flask_cors import CORS
from routes.corp import corp
from routes.department import department
import json
import base64

from flask_apscheduler import APScheduler
# from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask,request

import config
from config import app

from my_trigger import app
# app = Flask(__name__)
import datetime
import cv2
import numpy as np
from PIL import Image
import uuid
import os
# 路由
from routes.message import message
from routes.user import user
from routes.my import my
from routes.my_approve import my_approve
from routes.my_attendance import my_attendance
from routes.appeal import appeal
from routes.attendance import attendance
from routes.staff import staff

CORS(app, supports_credentials=True)
# CORS(app, resources=r'/*')
# app = Flask(__name__)

# 蓝图
app.register_blueprint(user, url_prefix="/user")
app.register_blueprint(corp, url_prefix="/corp")
app.register_blueprint(department, url_prefix="/department")
app.register_blueprint(staff, url_prefix="/staff")
app.register_blueprint(attendance, url_prefix="/attendance")
app.register_blueprint(appeal, url_prefix="/appeal")
# 蓝图 wechat
app.register_blueprint(message,url_prefix="/message")
app.register_blueprint(my_attendance,url_prefix="/my_attendance")
app.register_blueprint(my,url_prefix="/my")
app.register_blueprint(my_approve,url_prefix="/my_approve")



app.config['SECRET_KEY'] = config.SECRET_KEY

@app.route('/')
def ping():
    print("ping ok")
    return "12322o232k"


# @app.route('/get', methods=['POST'])
# def get():
#     print(request.get_data())
#
#     session['name']=request.values.get("name")
#     session['age']=request.values.get("age")
#
#     # queryRes=base_query_admission()
#     return json.dumps('ok', ensure_ascii=False)


if __name__ == '__main__':
    # from werkzeug.contrib.fixers import ProxyFix
    # app.wsgi_app = ProxyFix(app.wsgi_app)
    app.scheduler.start()
    app.run(host='0.0.0.0', port=5002, debug=True)
