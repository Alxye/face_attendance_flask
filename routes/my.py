from flask import Blueprint,request
my = Blueprint('my', __name__)
import json
import time
from models.user import *
from api.attendance import *
from api.AI_model import extract,calc_similarity
from api.department import *
from api.user import User_id_for_faceinfo
from datetime import date
import datetime

from models.attendance import Attendance
from my_trigger import app
import numpy as np


@my.route('/today_record',methods=['POST'])
def search_today_record():
    if request.method == 'POST':
        date_ = request.json.get('date')
        staffID = request.json.get('staffID')
        departmentID = request.json.get('departmentID')
        record = Attendance_search_today(staffID, date_)
        notice = Query_department_notice(departmentID)
        if record is not None:
            if (record.am_type == 1):
                clock_in_time = str(record.clock_in_time).split(' ')[1]
            else:
                clock_in_time = ''
            if (record.pm_type == 1):
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
                'notice': notice
            }
        else:
            am_type = 0
            pm_type = 0
            # new_record = Attendance_insert_today(am_type, pm_type, staffID, date_)
            # db.session.add(new_record)
            # db.session.commit()
            res = {
                'code': 1,
                'clock_in_time': '',
                'clock_out_time': '',
                'am_type': am_type,
                'pm_type': pm_type,
                'am_address': '',
                'pm_address': '',
                'notice': notice
            }
        return res
