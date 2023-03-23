# from operation.user import User_operation
import datetime
import time
import jwt
import config

from models.user import Users

import datetime
import time

from flask import jsonify

from operation.staff import staff_opration
from operation.user import User_opration
from utils.data_process import Class_To_Data
import jwt

# wechat ----------------------


def User_reg(username,staffID,departmentID,openid):
    u_o = User_opration()
    data = u_o._reg(username,staffID,departmentID,openid)
    return data

def User_search_userinfo(openid):
    u_o = User_opration()
    data = u_o._search_openid(openid)
    return data

def User_search_all():
    u_o = User_opration()
    data = u_o._all()
    return data

def User_id_check(staffID):
    u_o = User_opration()
    data = u_o._id_check(staffID)
    return data

def User_id_for_faceinfo(staffID):
    u_o = User_opration()
    data = u_o._id_faceinfo(staffID)
    return data

# wechat ----------------------

# def User_list():
#     u_o = User_operation()
#     data = u_o._all()
#     # data（复杂对象）====> 数据
#     data = Class_To_Data(data, u_o.__fields__, 0)
#     return data
#
#
# # def User_reg(kwargs):
# #     u_o = User_operation()
# #     data = u_o._reg(kwargs)
# #     return data
#
# 1112 ----> 123456

def User_list():
    u_o = User_opration()
    data = u_o._all()
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, u_o.__fields__, 0)
    print("api...")
    return data


def User_login2(name, pwd):
    u_o = User_opration()
    data = u_o.login(name, pwd)

    data = Class_To_Data(data, u_o.__fields__, 1)
    login_time = int(time.time())
    print(data['department_id'])
    if (pwd == data['password']):
        status = 1
        code = 200
        did = data['department_id']
    else:
        status = 0
        code = 300
        did = 0
    res = {
        "status": status,
        "code": code,
        "token": encode_auth_token(name, login_time),
        "did": did,
    }
    return jsonify(res)


def User_login(staff_id, password):
    # user_op = User_operation()
    # orig_data = user_op._login(employ_id)
    # state = 0  # 无该管理员
    # if orig_data is not None:
    #     data = Class_To_Data(orig_data, user_op.__fields__, 1)
    #     state = 1  # 有该管理员，但密码错误
    #     if password == data['password']:
    #         state = 2  # 密码正确
    #         login_time = int(time.time())
    #         orig_data['login_time'] = login_time
    #         user_op._update()
    #         token = self.encode_auth_token(userInfo.id, login_time)
    # return state
    # userInfo = Users.query.filter_by(staff_id=staff_id, type=2).first()
    userInfo = Users.query.filter_by(staff_id=staff_id).first()
    if userInfo is None:
        return 0, -1, ''
    elif userInfo.type is not 2:
        return 0, -1, ''
    else:
        # print(userInfo.password)
        if userInfo.password is None:
            userInfo.password=""
        # Users.set_password(Users, password)
        if Users.check_password(Users, userInfo.password, password):
            login_time = int(time.time())
            userInfo.login_time = login_time
            Users.update(userInfo)
            token = encode_auth_token(userInfo.id, login_time)
            return 2, userInfo.department_id, token
        else:
            return 1, -1, ''


def User_register(staff_id, password, department_id):
    userInfo = Users.query.filter_by(staff_id=staff_id).first()
    if userInfo is not None:
        return False, '同工号已被注册'
    newUser = Users(staff_id=staff_id, password=password, department_id=department_id, type=3)
    res = Users.add(Users, newUser)
    if newUser.id:
        return True, '注册成功'
    else:
        return False, '注册失败，服务异常'


def Admin_add(staff_id, department_id, type):
    userInfo = Users.query.filter_by(staff_id=staff_id).first()
    if userInfo is not None:
        return False, '同工号已存在'
    newUser = Users(staff_id=staff_id, password='123456', department_id=department_id, type=type)
    res = Users.add(Users, newUser)
    if newUser.id:
        return True, '新增成功'
    else:
        return False, '新增失败，服务异常'


def Admin_update(staff_id, staff_id_old, department_id, type):
    userInfo = Users.query.filter_by(staff_id=staff_id_old).first()
    newuserInfo = Users.query.filter_by(staff_id=staff_id).first()
    if userInfo is None:
        return False
    if staff_id != staff_id_old and newuserInfo is not None:
        return False
    else:
        userInfo.staff_id = staff_id
        userInfo.department_id = department_id
        userInfo.type = type
        Users.update(userInfo)
        return True


def User_changePW(staff_id, old_PW, new_PW):
    userInfo = Users.query.filter_by(staff_id=staff_id).first()
    if userInfo is None:
        return False, '查不到该用户'
    else:
        if Users.check_password(Users, userInfo.password, old_PW):
            userInfo.password = Users.set_password(Users, new_PW)
            Users.update(userInfo)
            return True, '修改成功'
        else:
            return False, '原密码错误'


def User_info(staff_id):
    userInfo = Users.query.filter_by(staff_id=staff_id).first()
    info = {
        'name': '',
        'age': -1,
        'staff_id': '',
        'department_id': -1
    }
    if userInfo is None:
        return 0, info
    else:
        info['name'] = userInfo.name
        info['age'] = userInfo.age
        info['staff_id'] = userInfo.staff_id
        info['department_id'] = userInfo.department_id
        return 1, info


def encode_auth_token(user_id, login_time):
    """
    生成认证Token
    :param user_id: int
    :param login_time: int(timestamp)
    :return: string
    """
    try:
        payload = {
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=0, seconds=10),
            'iat': datetime.datetime.utcnow(),
            'iss': 'ken',
            'data': {
                'id': user_id,
                'login_time': login_time
            }
        }
        return jwt.encode(
            payload,
            config.SECRET_KEY,
            algorithm='HS256'
        )
    except Exception as e:
        return e
