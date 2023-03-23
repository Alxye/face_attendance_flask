from flask import Blueprint, request, jsonify, json

from api.corporation import *

corp = Blueprint('corp', __name__)


@corp.route('/')
def ping():
    return '123ok'


@corp.route('/info', methods=['GET', 'POST'])
def info():
    res = Get()
    code = 404
    msg = ""
    if res is None:
        code = 401
        msg = "信息获取失败"
    else:
        code = 200
        msg = "信息获取成功"

    counts=countStaff()
    return_data = {
        "code": code,
        "data": res,
        "countStaff": counts,
        "msg": msg,
    }
    return jsonify(return_data)


@corp.route('/AdminData', methods=['GET'])
def AdminData():
    res = GetAdminData()
    code = 404
    msg = ""
    if res is None:
        code = 401
        msg = "信息获取失败"
    else:
        code = 200
        msg = "信息获取成功"
    return_data = {
        "code": code,
        "data": {
            'list':res,
            'pager':{
                'page':1,
                'pageSize':len(res),
                'total':len(res)
            }
        },
        "msg": msg,
    }
    return jsonify(return_data)


@corp.route('/update', methods=['POST'])
def update():
    data = json.loads(request.data)
    name = data['name']
    address = data['address']
    notice = data['notice']
    res = Update(name, address, notice)
    code = 404
    msg = ""
    if res is False:
        code = 401
        msg = "更新失败"
    else:
        code = 200
        msg = "更新成功"

    return_data = {
        "code": code,
        "msg": msg,
    }

    return jsonify(return_data)


@corp.route('/CountStaff', methods=['GET'])
def CountStaff():
    res = countStaff()
    code = 404
    msg = ""
    if res is 0:
        code = 401
        msg = "无员工！"
    else:
        code = 200
        msg = "获取成功"

    return_data = {
        "code": code,
        "data": res,
        "msg": msg,
    }
    return jsonify(return_data)


@corp.route('/getStaffDistribution', methods=['GET'])
def GetStaffDistribution():
    res = getStaffDistribution()
    code = 404
    msg = ""
    if res is None:
        code = 401
        msg = "获取失败"
    else:
        code = 200
        msg = "获取成功"

    return_data = {
        "code": code,
        "data": res,
        "msg": msg,
    }
    # print(return_data)

    return jsonify(return_data)
