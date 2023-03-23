from flask import Blueprint, request
from flask_cors import CORS, cross_origin

from api.appeal import *
import json
import time
from models.user import *
from api.appeal import *
import datetime

appeal = Blueprint('appeal', __name__)

@appeal.route('/submit',methods=['GET','POST'])
def apeeal_submit():
    if request.method == 'POST':
        # date, staffID, appeal_reason, time_state, category
        date_ = datetime.datetime.strptime(str(request.json.get('date')).replace('/','-'),"%Y-%m-%d")
        staffID = int(request.json.get('staffID'))
        appeal_reason = request.json.get('appeal_reason')
        morning_flag = request.json.get('morning_flag')
        category = int(request.json.get('category'))
        if(morning_flag=='false'):
            time_state = 1
        else:
            time_state = 0
        new_appeal = Appeal_submit(date_, staffID, appeal_reason, time_state, category)
        db.session.add(new_appeal)
        db.session.commit()
        return {
            'code': 1
        }

# @cross_origin()
@appeal.route('/list', methods=['POST'])
def read():
    # api的业务逻辑方法
    p = json.loads(request.data)
    page_index = p['page']
    page_size = p['pageSize']
    select_id = p['input']
    did=p['did']
    # data = get_all(page_index,page_size,select_id,did)
    data = get_all_by_department(page_index,page_size,select_id,did)
    # print(data)
    if select_id == '':
        total = data.__len__()
    else:
        total = data.__len__()
    res = {
        "code": 200,
        "data": data,
        "total": total
    }
    return res

@appeal.route('/create', methods=['POST'])
def create():
    # api的业务逻辑方法
    data = json.loads(request.data)
    d=create_appeal(data['staff_id'],data['state'],data['date'],data['appeal_reason'],data['reject_reason'])
    res = {
        "code": 200
    }
    return res

@appeal.route('/update', methods=['POST'])
def update():
    data = json.loads(request.data)
    print(data)
    id = data['id']
    rej=data['reject_reason']
    staff_id=data['staff_id']
    date=data['date']
    time_state=data['time_state']
    category=data['category']
    update_appeal(id,rej,staff_id,date,time_state,category)

    res = {
        "code": 200
    }
    return res

@appeal.route('/delete', methods=['POST'])
def delete():
    data = json.loads(request.data)
    id = data['id']
    d = delete_appeal(id)
    res = {
        "code": 200
    }
    return res
