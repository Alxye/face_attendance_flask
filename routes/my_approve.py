from flask import Blueprint, request

my_approve = Blueprint('my_approve', __name__)
import json
import time
from models.user import *
from api.my_approve import *
from api.AI_model import extract, calc_similarity
from api.department import Query_department_attendance_time
from api.user import User_id_for_faceinfo
from datetime import date
import datetime

import numpy as np


@my_approve.route('/apply', methods=['POST'])
def appeal_submit():
    if request.method == 'POST':
        startDate = request.json.get('startDate')
        endDate = request.json.get('endDate')
        startAmPm = request.json.get('startAmPm')
        endAmPm = request.json.get('endAmPm')
        staffID = int(request.json.get('staffID'))
        appeal_reason = request.json.get('appeal_reason')
        category = int(request.json.get('category'))
        print('---------my_approve_apply---------')
        print(startDate)
        print(startAmPm)
        print(endDate)
        print(endAmPm)
        d = datetime.datetime.strptime(str(startDate).replace('/', '-'), "%Y-%m-%d")
        delta = datetime.timedelta(days=1)
        while 1:
            print(d.strftime("%Y-%m-%d"))
            if str(d.strftime("%Y-%m-%d")) == startDate:
                if startAmPm == '上班':
                    new_appeal = my_approve_submit(d, staffID, appeal_reason, 0, category)
                    db.session.add(new_appeal)
                if str(d.strftime("%Y-%m-%d")) == endDate and endAmPm == '上班':
                    break
                new_appeal = my_approve_submit(d, staffID, appeal_reason, 1, category)
                db.session.add(new_appeal)
                if str(d.strftime("%Y-%m-%d")) == endDate:
                    break
            elif str(d.strftime("%Y-%m-%d")) == endDate:
                new_appeal = my_approve_submit(d, staffID, appeal_reason, 0, category)
                db.session.add(new_appeal)
                if endAmPm == '下班':
                    new_appeal = my_approve_submit(d, staffID, appeal_reason, 1, category)
                    db.session.add(new_appeal)
                break
            else:
                new_appeal = my_approve_submit(d, staffID, appeal_reason, 0, category)
                db.session.add(new_appeal)
                new_appeal = my_approve_submit(d, staffID, appeal_reason, 1, category)
                db.session.add(new_appeal)
            d.strftime("%Y-%m-%d")
            d += delta

        db.session.commit()

        return {
            'code': 1
        }

@my_approve.route('/get', methods=['POST'])
def appeal_get():
    if request.method == 'POST':
        staffID = int(request.json.get('staffID'))
        record = my_approve_get(staffID)
        List = []
        for item in record:
            List.append({
                'Date': str(item.date).split(' '),
                'AmPm': item.time_state,
                'category': item.category,
                'applyStatus': item.state,
                'reject_reason': item.reject_reason

            })

        res = {
            'List': List,
            'len': len(List)
        }

        return res









