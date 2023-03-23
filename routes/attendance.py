
import json

import pandas as pd
from flask import Blueprint, request, make_response, send_file

from api.attendance import *

attendance = Blueprint('attendance', __name__)

import json
import time
from models.user import *
from api.AI_model import extract, calc_similarity
from api.department import Query_department_attendance_time, Query_department_attendance_time2
from api.user import User_id_for_faceinfo
import datetime

from models.attendance import Attendance
from my_trigger import app
import numpy as np


# wechat -----------

def judge(time_,clock_start,clock_end):
    start_second = int(clock_start.split(':')[0]) * 3600 + int(clock_start.split(':')[1]) * 60 + int(
        clock_start.split(':')[2])
    end_second = int(clock_end.split(':')[0]) * 3600 + int(clock_end.split(':')[1]) * 60 + int(
        clock_end.split(':')[2])
    now_second = int(time_.split(':')[0]) * 3600 + int(time_.split(':')[1]) * 60 + int(
        time_.split(':')[2])
    if(now_second>=start_second and now_second<=end_second):
        return True
    else:
        return False

@attendance.route('/judge_morning_flag',methods=['POST'])
def judge_morning_flag():
    if request.method == 'POST':
        now = datetime.datetime.now()
        departmentID = int(request.json.get('departmentID'))
        _,time1,time2,_ = Query_department_attendance_time2(departmentID)
        time1 = str(time1)
        time1_second = int(time1.split(':')[0]) * 3600 + int(time1.split(':')[1]) * 60 + int(
            time1.split(':')[2])
        now_second = int(now.hour) * 3600 + int(now.minute) * 60 + int(
            now.second)
        if(time1_second + 3600) >= now_second:
            return {
                'code': 1
            }
        else:
            return{
            'code': 0
        }



@attendance.route('/today_record',methods=['POST'])
def search_today_record():
    if request.method == 'POST':
        date_ = request.json.get('date')
        staffID = request.json.get('staffID')
        record = Attendance_search_today(staffID,date_)
        if record is not None:
            if (record.am_type != 0):
                clock_in_time = str(record.clock_in_time).split(' ')[1]
            else:
                clock_in_time = ''
            if (record.pm_type != 0):
                clock_out_time = str(record.clock_out_time).split(' ')[1]
            else:
                clock_out_time = ''

            res = {
                'code': 1,
                'clock_in_time':  clock_in_time,
                'clock_out_time': clock_out_time,
                'am_type': record.am_type,
                'pm_type': record.pm_type,
                'am_address': record.am_address,
                'pm_address': record.pm_address,
            }
        else:
            am_type = 0
            pm_type = 0
            new_record = Attendance_insert_today(am_type, pm_type, staffID, date_)
            db.session.add(new_record)
            db.session.commit()
            res = {
                'code': 1,
                'clock_in_time': '',
                'clock_out_time': '',
                'am_type': am_type,
                'pm_type': pm_type,
                'am_address': '',
                'pm_address': '',
            }
        # print(res)
        return res

@attendance.route('/update_info',methods=['POST'])
def update_info():
    if request.method == 'POST':
        staffID = int(request.form.get('staffId'))
        morning_flag = int(request.form.get('morning_flag'))
        date_ = request.form.get('date')
        time_ = request.form.get('time')
        address = request.form.get('address')
        departmentID = int(request.form.get('departmentID'))
        files = request.files.get('files')
        res = {}
        # 逻辑判断 人脸识别 + 时间判断
        # 时间判断
        # print(morning_flag)
        clock_start,clock_end = Query_department_attendance_time(departmentID,morning_flag)
        clock_start = str(clock_start)
        clock_end = str(clock_end)
        # 人脸判断:
        record_faceinfo = np.frombuffer(User_id_for_faceinfo(staffID), dtype=np.float32)
        time_str = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        tmp_save_add = f'static/tmp/{staffID}_{time_str}.jpg'
        files.save(tmp_save_add)
        ans = extract(tmp_save_add)
        if(ans['code']==0):
            res['code']=0
        else:
            new_faceinfo = ans['embedding']
            # print(extract(tmp_save_add))
            new_faceinfo = np.frombuffer(new_faceinfo, dtype=np.float32)
            similarity = calc_similarity(record_faceinfo, new_faceinfo)
            print(similarity)
            if similarity < 0.55:
                s = date_.replace('/', '-') + ' ' + time_
                datetime_ = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
                record = Attendance_search_today(staffID=staffID, date=date_)
                if(morning_flag==1):
                    end_second = int(clock_end.split(':')[0]) * 3600 + int(clock_end.split(':')[1]) * 60 + int(
                        clock_end.split(':')[2])
                    now_second = int(time_.split(':')[0]) * 3600 + int(time_.split(':')[1]) * 60 + int(
                        time_.split(':')[2])
                    if(end_second>=now_second):
                        res['code'] = 1
                        if (morning_flag):
                            record.clock_in_time = datetime_
                            record.am_type = 1
                            record.am_address = address
                        else:
                            record.clock_out_time = datetime_
                            record.pm_type = 1
                            record.pm_address = address
                        db.session.add(record)
                        db.session.commit()
                    elif(end_second+3600>=now_second):
                        res['code'] = 2
                        if (morning_flag):
                            record.clock_in_time = datetime_
                            record.am_type = 2
                            record.am_address = address
                        else:
                            record.clock_out_time = datetime_
                            record.pm_type = 2
                            record.pm_address = address
                        db.session.add(record)
                        db.session.commit()
                    else:
                        res['code'] = 0
                else:
                    start_second = int(clock_start.split(':')[0]) * 3600 + int(clock_start.split(':')[1]) * 60 + int(
                        clock_start.split(':')[2])
                    now_second = int(time_.split(':')[0]) * 3600 + int(time_.split(':')[1]) * 60 + int(
                        time_.split(':')[2])
                    if (start_second <= now_second):
                        res['code'] = 1
                        if (morning_flag):
                            record.clock_in_time = datetime_
                            record.am_type = 1
                            record.am_address = address
                        else:
                            record.clock_out_time = datetime_
                            record.pm_type = 1
                            record.pm_address = address
                        db.session.add(record)
                        db.session.commit()
                    elif (start_second - 3600 <= now_second):
                        res['code'] = 2
                        if (morning_flag):
                            record.clock_in_time = datetime_
                            record.am_type = 2
                            record.am_address = address
                        else:
                            record.clock_out_time = datetime_
                            record.pm_type = 2
                            record.pm_address = address
                        db.session.add(record)
                        db.session.commit()
                    else:
                        res['code'] = 0
            else:
                res['code'] = 0
        return res


# wechat -----------

# @cross_origin()
@attendance.route('/list', methods=['POST'])
def read():
    # api的业务逻辑方法
    print(request.data)
    p = json.loads(request.data)
    page_index = p['page']
    page_size = p['pageSize']
    select_id = p['input']
    date = p['date']
    did = p['did']
    print(date)
    data = get_all(page_index, page_size, select_id, date, did)
    print(data)

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


@attendance.route('/create', methods=['POST'])
def create():
    # api的业务逻辑方法
    data = json.loads(request.data)
    res = create_attendance(data['staff_id'], data['date'], data['am_type'], data['pm_type'], data['clock_in_time'],
                            data['clock_out_time'])

    res = {
        "code": 200
    }
    return res


@attendance.route('/update', methods=['POST'])
def update():
    data = json.loads(request.data)
    id = data['staff_id']
    d = update_attendance(id, data['date'], data['am_type'], data['pm_type'], data['clock_in_time'],
                          data['clock_out_time'])
    res = {
        "code": 200
    }
    return res


@attendance.route('/delete', methods=['POST'])
def delete():
    data = json.loads(request.data)
    id = data['staff_id']
    data = delete_attendance(id, data['date'])
    res = {
        "code": 200
    }
    return res


@attendance.route('/monthChart', methods=['POST'])
def month():
    data = json.loads(request.data)
    did = data['did']
    data = get_attendance(id)
    print(data)
    res = {
        "code": 200,
        "data": data
    }
    return res


@attendance.route('/dayChart', methods=['POST'])
def day():
    data = json.loads(request.data)
    did = data['did']
    data = get_attend(did)
    print(data)
    res = {
        "code": 200,
        "data": data
    }
    return res


@attendance.route('/chartCheckin', methods=['POST'])
def checkin():
    data = json.loads(request.data)
    did = data['did']
    time = data['select_month']
    select_month = datetime.datetime.strptime(time, '%Y-%m')
    data = get_checkin(did, select_month)
    print(data)
    res = {
        "code": 200,
        "data": data
    }
    return res


@attendance.route('/chartCheckin0', methods=['POST'])
def checkin0():
    data = json.loads(request.data)
    did = data['did']
    time = data['select_month']
    select_month = datetime.datetime.strptime(time, '%Y-%m')
    data = get_checkin0(did, select_month)
    print(data)
    res = {
        "code": 200,
        "data": data
    }
    return res


@attendance.route('/chartCheckin2', methods=['POST'])
def checkin2():
    data = json.loads(request.data)
    did = data['did']
    time = data['select_month']
    select_month = datetime.datetime.strptime(time, '%Y-%m')
    data = get_checkin2(did, select_month)
    print(data)
    res = {
        "code": 200,
        "data": data
    }
    return res


@attendance.route('/chartCheckout', methods=['POST'])
def checkout():
    data = json.loads(request.data)
    did = data['did']
    time = data['select_month']
    select_month = datetime.datetime.strptime(time, '%Y-%m')
    data1 = checkout1(did, select_month)
    data0 = checkout0(did, select_month)
    data2 = checkout2(did, select_month)
    data = []
    data.append(data1)
    data.append(data0)
    data.append(data2)

    print(data)
    res = {
        "code": 200,
        "data": data
    }
    return res


@attendance.route('/excel', methods=['POST'])
def get_excel():
    data = json.loads(request.data)
    id = data['did']
    date = data['date']
    data = excel(id, date)
    df = pd.DataFrame(data)
    df.to_excel("demo.xlsx", index=False)
    res = {
        "code": 200,
        "data": df
    }
    response = make_response(send_file('demo.xlsx', as_attachment=True))
    response.headers["Access-Control-Expose-Headers"] = "Content-disposition"
    return response
