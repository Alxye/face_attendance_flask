import time,datetime

from flask import jsonify

from operation.attendance import attendance_opration
from utils.data_process import Class_To_Data

now=datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S ")

# wechat

def Attendance_search_today(staffID,date):
    A_o = attendance_opration()
    data = A_o._search_today_record(staffID, date)
    return data

def Attendance_insert_today(am_type, pm_type, staffID, date):
    A_o = attendance_opration()
    data = A_o._insert_today_record(am_type, pm_type, staffID, date)
    return data

def Attendance_auto_insert(staffID, date):
    A_o = attendance_opration()
    data = A_o._auto_insert_record(staffID, date)
    return data


def get_all(i,s,id,date,did):
    a_o = attendance_opration()
    data = a_o._all(i,s,id,date,did)
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, a_o.__fields__, 0)
    return data

def create_attendance(staff_id,date,am_type,pm_type,clock_in_time,clock_out_time):
    a_o = attendance_opration()
    data = a_o.create(staff_id,date,am_type,pm_type,clock_in_time,clock_out_time)
    # data（复杂对象）====> 数据
    #data = Class_To_Data(data, s_o.__fields__, 0)
    return data

def update_attendance(staff_id,date,am_type,pm_type,ic=now,oc=now):
    a_o = attendance_opration()
    data = a_o.update(staff_id,date,am_type,pm_type,ic,oc)

    return data

def delete_attendance(id,date):
    s_o = attendance_opration()
    data = s_o.delete(id,date)

    return data

def get_total_number(did,id,date):
    s_o = attendance_opration()
    return s_o.get_total_number(did,id,date)

def get_attendance(did):
    s_o = attendance_opration()
    return s_o.get_attendanceByMonth(did)



def get_checkin(did,month):
    s_o = attendance_opration()
    return s_o.get_checkinByDay(did,month)
def get_checkin0(did,month):
    s_o = attendance_opration()
    return s_o.get_checkinByDay0(did,month)
def get_checkin2(did,month):
    s_o = attendance_opration()
    return s_o.get_checkinByDay2(did,month)
def checkout1(did,month):
    s_o = attendance_opration()
    return s_o.checkoutByDay1(did,month)
def checkout0(did,month):
    s_o = attendance_opration()
    return s_o.checkoutByDay0(did,month)
def checkout2(did,month):
    s_o = attendance_opration()
    return s_o.checkoutByDay2(did,month)



def get_attend(did):
    s_o = attendance_opration()
    return s_o.get_attendanceByDay(did)

def excel(did,date,staff_id):
    a_o = attendance_opration()
    data = a_o.get_alldata(did,date,staff_id)
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, a_o.__fields__, 0)


    return data
