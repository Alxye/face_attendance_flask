from flask import Blueprint, request, jsonify, json

from api.department import *
import time
import json

department = Blueprint('department', __name__)


@department.route('/', methods=['GET'])
def ping():
    return 'department ok!'


# wechat----------
@department.route('/all', methods=['GET', 'POST'])
def department_search():
    if request.method == 'POST':
        department_list = Department_all()
        lists = []
        for i in department_list:
            lists.append(i.department_name)
        res = {
            'code': 1,
            'list': lists
        }
        return res


@department.route('/location_get', methods=['GET', 'POST'])
def department_location_get():
    if request.method == 'POST':
        departmentID = int(request.json.get('departmentID'))
        longitude, latitude = Query_department_location(departmentID)
        res = {
            'code': 1,
            'longitude': longitude,
            'latitude': latitude
        }
        return res


# wechat----------

@department.route('/info', methods=['GET'])
def info():
    res = Get_departmentInfo()
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
    print(return_data)
    return jsonify(return_data)


@department.route('/add', methods=['POST'])
def add():
    data = json.loads(request.data)
    name = data['department_name']
    notice = data['notice']
    exist = Is_departmentExist(name)
    code = 404
    msg = ""
    if exist is True:
        res = False
        msg = "部门已存在"
    else:
        res = Add_department(name, notice)
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


@department.route('/dashboardCard', methods=['POST'])
def dashboard_card():
    data = json.loads(request.data)
    department_id = data['department_id']
    print(">>>>>>>>>>", department_id)
    department_name = Get_departmentName(department_id)
    appealstaffcount = Count_AppealStaff(department_id)
    appealattendancecount = Count_AppealAttendance(department_id)
    code = 200
    return_data = {
        "code": code,
        "data": {
            "department_name": department_name,
            "appealstaffcount": appealstaffcount,
            "appealattendancecount": appealattendancecount
        }
    }

    print(">>>>>>>>>>", return_data)

    return jsonify(return_data)


@department.route('/update', methods=['POST'])
def update():
    data = json.loads(request.data)
    department_id = data['id']
    name = data['name']
    notice = data['notice']
    longitude = data['longitude']
    latitude = data['latitude']
    address = data['address']
    clock_in_start = time.strptime("2023-01-01 " + data['clock_in_start'], "%Y-%m-%d %H:%M:%S")
    clock_in_end = time.strptime("2023-01-01 " + data['clock_in_end'], "%Y-%m-%d %H:%M:%S")
    clock_out_start = time.strptime("2023-01-01 " + data['clock_out_start'], "%Y-%m-%d %H:%M:%S")
    clock_out_end = time.strptime("2023-01-01 " + data['clock_out_end'], "%Y-%m-%d %H:%M:%S")
    print(Get_departmentName(department_id))
    print(name)
    if Get_departmentName(department_id) != name:
        isExist = Is_departmentExist(name)
        if isExist:
            code = 401
            msg = "不能更名为已有部门"
        else:
            res = Update(department_id, name, notice, clock_in_start, clock_in_end, clock_out_start, clock_out_end,
                         longitude=longitude, latitude=latitude, address=address)
            if res:
                code = 200
                msg = "更新成功"
            else:
                code = 401
                msg = "更新失败"
    else:
        res = Update(department_id, name, notice, clock_in_start, clock_in_end, clock_out_start, clock_out_end,
                     longitude=longitude, latitude=latitude, address=address)
        if res:
            code = 200
            msg = "更新成功"
        else:
            code = 401
            msg = "更新失败"
    return_data = {
        "code": code,
        'msg': msg
    }
    return jsonify(return_data)


@department.route('/delete', methods=['POST'])
def delete():
    data = json.loads(request.data)
    department_id = data['id']
    count = Count_DepartmentStaff(department_id)
    if count is not 0:
        code = 401
        msg = "该部门尚有待审核的员工、管理员或正式员工"
    else:
        res = Department.delete(Department, department_id)
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
