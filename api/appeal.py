import time

from flask import jsonify

from operation.appeal import appeal_opration
from operation.staff import staff_opration
from operation.attendance import attendance_opration
from utils.data_process import Class_To_Data

def Appeal_submit(date, staffID, appeal_reason, time_state, category):
    A_o = appeal_opration()
    data = A_o._submit(date, staffID, appeal_reason, time_state, category)
    return data

def get_all(i,s,id,did):
    s_o = appeal_opration()
    data = s_o._all_by_department(i,s,id,did)
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, s_o.__fields__, 0)
    return data

def get_all_by_department(i,s,id,did):
    s_o = appeal_opration()
    u_o = staff_opration()
    data = s_o._all_by_department(i,s,id,did)
    # data（复杂对象）====> 数据
    # fields=list(set(s_o.__fields__+u_o.__fields__))
    list=[]
    for i in range(0,len(data)):
        obj1=Class_To_Data(data[i][0], s_o.__fields__, 1)
        obj2=Class_To_Data(data[i][1], u_o.__fields__, 1)
        obj2.update(obj1)
        list.append(obj2)
    # print(list)
    return list

def create_appeal(staff_id,state,appeal_reason,reject_reason,date):
    s_o = appeal_opration()
    data = s_o.create(staff_id,state,appeal_reason,reject_reason,date)

    return data

def update_appeal(id,rej,staff_id,date,time_state,category):
    s_o = appeal_opration()
    a_o = attendance_opration()
    data = s_o.update(id,rej)
    if rej=='':
        if time_state==0:
            if a_o.exist(staff_id=staff_id,date=date) is False:
                a_o.create_attendance(staff_id=staff_id,date=date,am_type=1,pm_type=0)
            else:
                a_o.update_amclock_state(staff_id=staff_id,date=date,am_type=1)
        elif time_state==1:
            if a_o.exist(staff_id=staff_id,date=date) is False:
                a_o.create_attendance(staff_id=staff_id,date=date,am_type=0,pm_type=1)
            else:
                a_o.update_pmclock_state(staff_id=staff_id,date=date,pm_type=1)
    return data

# # tyz 0322
# def update_appeal(id,rej,sid,date,ts):
#     s_o = appeal_opration()
#     data = s_o.update(id,rej,sid,date,ts)
#
#     return data

def delete_appeal(id):
    s_o = appeal_opration()
    data = s_o.delete(id)

    return data
def get_total_number():
    s_o = appeal_opration()
    return s_o.get_total_number()

