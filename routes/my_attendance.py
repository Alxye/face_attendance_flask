from flask import Blueprint, request

my_attendance = Blueprint('my_attendance', __name__)
import json
import time
from models.user import *
from api.my_attendance import *
from api.AI_model import extract, calc_similarity
from api.department import Query_department_attendance_time
from api.user import User_id_for_faceinfo
from datetime import date
import datetime

import numpy as np

@my_attendance.route('/all_record', methods=['POST'])
def search_today_record():
    if request.method == 'POST':
        staffID = request.json.get('staffID')
        record = Attendance_search_all(staffID)
        print('---------my_attendance_all_record---------')
        List = []
        lack_num = 0
        late_num = 0
        eaerly_num = 0
        for item in record:
            inStatus = "正常"
            if item.am_type == 0:
                inStatus = "缺卡"
                lack_num += 1
            elif item.am_type == 2:
                inStatus = "迟到"
                late_num += 1
            outStatus = "正常"
            if item.pm_type == 0:
                outStatus = "缺卡"
                lack_num += 1
            elif item.pm_type == 2:
                outStatus = "早退"
                eaerly_num += 1
            List.append({
                "day": str(item.date),
                "inStatus": inStatus,
                "outStatus": outStatus
            })

        List.reverse()
        res = {
            'List': List,
            'lack_num': lack_num,
            'early_num': eaerly_num,
            'late_num': late_num
        }
        return res
