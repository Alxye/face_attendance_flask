from flask import Blueprint, request, jsonify
from flask_cors import CORS, cross_origin

from api.staff import get_allstaff, create_staff, update_staff, delete_staff, get_total_number,get_total_number_by_department
import json

staff = Blueprint('staff', __name__)


# @cross_origin()
@staff.route('/list', methods=['POST'])
def read():
    # api的业务逻辑方法
    p = json.loads(request.data)
    page_index=p['page']
    page_size=p['pageSize']
    select_id=p['input']
    did=p['did']
    data = get_allstaff(page_index,page_size,select_id,did)

    print(data)
    if select_id=='':
        # total=get_total_number(did)
        total=get_total_number_by_department(did)
    else:
        total=data.__len__()
    res={
        "code":200,
        "data":data,
        "total":total
    }
    return res

@staff.route('/create', methods=['POST'])
def create():
    # api的业务逻辑方法
    data = json.loads(request.data)
    print(data)
    d=create_staff(data['staff_id'],data['name'],data['age'],data['department_id'],data['type'])
    res = {
        "code": 200 if d is True else False,
        'msg':"新增失败" if d is False else True
    }
    return res

@staff.route('/update', methods=['POST'])
def update():
    data = json.loads(request.data)
    id = data['staff_id']
    d=update_staff(id=id,
                   name=data['name'],
                   type=data['type'],
                   age=data['age'],
                   did=data['department_id'])
    res={
        "code":200
    }
    return res

@staff.route('/delete', methods=['POST'])
def delete():
    data = json.loads(request.data)
    id = data['staff_id']
    data = delete_staff(id)
    res={
        "code":200
    }
    return res
