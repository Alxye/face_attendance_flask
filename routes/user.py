from flask import Blueprint, request, jsonify, json
from flask import Blueprint, request
from flask_cors import CORS, cross_origin
import json
import time
from api.user import *
import hashlib
import json,requests
from WXBizDataCrypt import WXBizDataCrypt
from flask import Flask
from config import db_init as db
from models.department import *
from models.user import *
import os
import datetime
from api.AI_model import *
from api.department import *
from config import *


user = Blueprint('user', __name__)

from api.user import *
from api.department import *

# wechat ---------------

@user.route('/wxlogin', methods=['GET','POST'])
def user_wxlogin():
    # md5 = hashlib.md5()
    data = json.loads(request.get_data().decode('utf-8')) # 将前端Json数据转为字典
    code = data['platCode'] # 前端POST过来的微信临时登录凭证code
    # encryptedData = data['platUserInfoMap']['encryptedData']
    # iv = data['platUserInfoMap']['iv']
    req_params = {
        'appid': appID,
        'secret': appSecret,
        'js_code': code,
        'grant_type': 'authorization_code'
    }
    wx_login_api = 'https://api.weixin.qq.com/sns/jscode2session'
    response_data = requests.get(wx_login_api, params=req_params) # 向API发起GET请求
    resData = response_data.json()
    # errcode = resData['errcode'] if 'errcode' in resData else None
    # if errcode:
    #     res = {
    #         'code': 13001,
    #         'msg': 'code2Session:' + resData.errmsg
    #     }
    # else:
    openid = resData['openid']  # 得到用户关于当前小程序的OpenID

    # md5.update(openid.encode('utf-8'))  # 要对哪个字符串进行加密，就放这里
    # openid = md5.hexdigest()
    # session_key = resData['session_key']  # 得到用户关于当前小程序的会话密钥session_key
    # pc = WXBizDataCrypt(appID, session_key)  # 对用户信息进行解密
    # userinfo = pc.decrypt(encryptedData, iv)  # 获得用户信息
    userinfo = {}
    userinfo['openid'] = openid
    userlist = User_search_userinfo(openid)
    if userlist is not None:
        type = int(userlist.type)
        if(type!=0):
            userinfo['username'] = userlist.name
            userinfo['staffID'] = userlist.staff_id
            userinfo['departmentID'] = userlist.department_id
            res = {
                'code': 10000,
                'userinfo': userinfo
            }
        else:
            res = {
                'code': 10001,
                'userinfo': userinfo
            }
    else:
        print('user does not exit')
        res = {
            'code': 10002,
            'userinfo': userinfo
        }
    return res


@user.route('/register',methods=['GET','POST'])
def user_register():
    if request.method == 'POST':
        username = request.form.get('username')
        staffID = int(request.form.get('staffID'))
        departmentname = request.form.get('departmentname')
        departmentid = Query_department_id(departmentname)
        openid = request.form.get('openid')
        files = request.files.get('files')
        time_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        tmp_save_add = f'static/tmp/{staffID}_{time_str}.jpg'
        files.save(tmp_save_add)
        res = extract(tmp_save_add)
        ans = {}
        if (res['code'] == 1):
            new_user = User_reg(username, staffID, departmentid, openid, res['embedding'])
            db.session.add(new_user)
            db.session.commit()
            ans['state'] = 1
        else:
            ans['state'] = 0
        return ans

@user.route('/id_check',methods=['GET','POST'])
def user_id_check():
    if request.method == 'POST':
        staffID = int(request.json.get('staffID'))
        user_list = User_id_check(staffID)
        if user_list is None:
            res = {
                'code': 1
            }
        else:
            res = {
                'code': 0
            }
        return res

# wechat ---------------


# tyz
# @cross_origin()
@user.route('/list', methods=['GET'])
def list():
    # api的业务逻辑方法
    data = User_list()
    return data


@user.route('/', methods=['GET'])
def ping():
    # api的业务逻辑方法
    # data = User_list()
    return 'user ping'

@user.route('/login', methods=['GET', 'POST'])
def admin_login():
    data = json.loads(request.data)
    staff_id = data['staff_id']
    password = data['password']
    if not staff_id or not password:
        return jsonify(False, '', '用户名和密码不能为空')
    res, department_id, token = User_login(staff_id, password)
    department_name = Get_departmentName(department_id)
    code = 404
    msg = ""
    if res == 0:
        code = 401
        msg = "管理员不存在或无权限"
    elif res == 1:
        code = 401
        msg = "管理员密码错误"
    elif res == 2:
        code = 200
        msg = "登录成功"

    return_data = {
        "code": code,
        "data": {
            "token": token,
            "info": {
                'staff_id': staff_id,
                'department_id': department_id,
                'department_name': department_name
            }
        },
        "msg": msg,
    }

    return jsonify(return_data), 200


@user.route('/admin_register', methods=['POST'])
def admin_register():
    data = json.loads(request.data)
    staff_id = data['staff_id']
    password = data['password']
    department_name = data['department_name']
    department_id = Get_departmentId(department_name)
    res, msg = User_register(staff_id, password, department_id)

    if res is False:
        code = 401
    else:
        code = 200

    return_data = {
        "code": code,
        "msg": msg,
    }
    return jsonify(return_data), 200


@user.route('/addAdmin', methods=['POST'])
def addAdmin():
    data = json.loads(request.data)
    staff_id = data['staff_id']
    type = data['type']
    department_id = data['department_id']
    res, msg = Admin_add(staff_id, department_id, type)
    if res is False:
        code = 401
    else:
        code = 200

    return_data = {
        "code": code,
        "msg": msg,
    }
    return jsonify(return_data), 200


@user.route('/updateAdmin', methods=['POST'])
def updateAdmin():
    data = json.loads(request.data)
    staff_id = data['staff_id']
    staff_id_old = data['staff_id_old']
    type = data['type']
    department_id = data['department_id']
    res = Admin_update(staff_id=staff_id,staff_id_old=staff_id_old, department_id=department_id, type=type)
    if res is False:
        code = 401
    else:
        code = 200

    return_data = {
        "code": code,
    }
    return jsonify(return_data), 200


@user.route('/deleteAdmin', methods=['POST'])
def deleteAdmin():
    data = json.loads(request.data)
    staff_id = data['staff_id']
    res = Users.delete(Users, staff_id)
    if res is None:
        code = 200
        msg = "删除成功"
    else:
        code = 401
        msg = "删除失败"
    return_data = {
        "code": code,
        'msg': msg
    }
    return jsonify(return_data)


@user.route('/info', methods=['GET', 'POST'])
def admin_info():
    data = json.loads(request.data)
    staff_id = data['staff_id']
    res, info = User_info(staff_id)
    code = 404
    msg = ""
    if res is 0:
        code = 401
        msg = "信息获取失败"
    elif res is 1:
        code = 200
        msg = "信息获取成功"
        department_name = Get_departmentName(info['department_id'])
        info['department_name'] = department_name

    return_data = {
        "code": code,
        "data": {
            "info": info
        },
        "msg": msg,
    }

    return jsonify(return_data)


@user.route('/logout', methods=['GET', 'POST'])
def admin_logout():
    return_data = {
        "code": 200,
        "data": {},
        "msg": "success",
    }
    return jsonify(return_data)


@user.route('/pwd_change', methods=['POST'])
def pwd_change():
    data = json.loads(request.data)
    print(data)
    staff_id = data['staff_id']
    new = data['new']
    old = data['old']
    code = 404
    msg = ''
    if old == new:
        msg = "新旧密码不能相同"
    else:
        res, msg = User_changePW(staff_id, old, new)
        if res is True:
            code = 200
        else:
            code = 202
    return_data = {
        "code": code,
        "msg": msg,
    }
    return jsonify(return_data)


@user.route('/reg', methods=['POST'])
def reg():
    data = json.loads(request.data)

    # data = User_reg({
    #     "sername": data['name']
    #
    # })
    return "123"
