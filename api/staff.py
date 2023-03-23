import time

from flask import jsonify

from operation.staff import staff_opration
from utils.data_process import Class_To_Data

def get_allstaff(i,s,id,did):
    s_o = staff_opration()
    data = s_o._all(i,s,id,did)
    # data（复杂对象）====> 数据
    data = Class_To_Data(data, s_o.__fields__, 0)
    return data

def create_staff(staff_id,name,age,department_id,type):
    s_o = staff_opration()
    staff_info = s_o.get_by_staff_id(staff_id=staff_id)
    if not staff_info:
        data = s_o.create(staff_id,name,age,department_id,type)
        return True
    else:
        return False


def update_staff(id,name,age,did,type):
    s_o = staff_opration()
    data = s_o.update(id,name,age,did,type)

    return data

def delete_staff(id):
    s_o = staff_opration()
    data = s_o.delete(id)

    return data

def get_total_number(did):
    s_o = staff_opration()
    return s_o.get_total_number(did)

def get_total_number_by_department(did):
    s_o = staff_opration()
    return s_o.get_total_number_by_department(did)

