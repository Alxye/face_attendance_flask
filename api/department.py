import datetime

from models.department import Department
from models.user import Users
from models.attendance_appeal import AttendanceAppeal
from api.corporation import countStaff
from operation.department import department_operation


# wechat -----------------------

def Department_all():
    D_o = department_operation()
    data = D_o._all()
    return data


def Query_department_attendance_time(departmentID,morning_flag):
    D_o = department_operation()
    data = D_o._query_attendance_time(department_id=departmentID,morning_flag=morning_flag)
    return data

def Query_department_id(departmentname):
    D_o = department_operation()
    data = D_o._query_departmentid_from_name(departmentname)
    return data

def Query_department_attendance_time2(departmentID):
    D_o = department_operation()
    data = D_o._query_attendance_time2(department_id=departmentID)
    return data
# wechat -----------------------

def Update(department_id, department_name, notice, clock_in_start, clock_in_end, clock_out_start, clock_out_end):
    depInfo = Department.query.filter_by(department_id=department_id).first()
    if depInfo is None:
        return False
    else:
        depInfo.department_name = department_name
        depInfo.notice = notice
        depInfo.clock_in_start = clock_in_start
        depInfo.clock_in_end = clock_in_end
        depInfo.clock_out_start = clock_out_start
        depInfo.clock_out_end = clock_out_end
        res = Department.update(depInfo)
        print(res)
        return True if res is None else False


def Get_departmentName(department_id):
    departmentInfo = Department.get(Department, department_id)
    if departmentInfo is None:
        return ''
    else:
        return departmentInfo.department_name

def Get_departmentId(department_name):
    departmentInfo = Department.findWithName(Department, department_name)
    if departmentInfo is None:
        return None
    else:
        return departmentInfo.department_id


def Is_departmentExist(department_name):
    departmentInfo = Department.findWithName(Department, department_name)
    if departmentInfo is None:
        return False
    else:
        return True


def Count_AppealStaff(department_id):
    return Users.query.filter_by(department_id=department_id, type=0).count()

def Count_DepartmentStaff(department_id):
    return Users.query.filter_by(department_id=department_id).count()


def Count_AppealAttendance(department_id):
    res = AttendanceAppeal.query.filter_by(state=0). \
        outerjoin(Users, AttendanceAppeal.staff_id == Users.staff_id). \
        add_entity(Users).filter(Users.department_id == department_id). \
        count()
    return res


def Add_department(name, notice):
    newDep = Department(department_name=name, notice=notice)
    res = Department.add(Department, newDep)
    if newDep.department_id:
        return True
    else:
        return False

#
# def Delete_department(department_id):
#     depInfo = Department.query.filter_by(department_id=department_id).first()
#     if depInfo is None:
#         return False
#     else:
#         depInfo.department_name = department_name
#         depInfo.notice = notice
#         depInfo.clock_in_start = clock_in_start
#         depInfo.clock_in_end = clock_in_end
#         depInfo.clock_out_start = clock_out_start
#         depInfo.clock_out_end = clock_out_end
#         res = Department.update(depInfo)
#         print(res)
#         return True if res is None else False
#


def Get_departmentInfo():
    department_info_group = Department.query.all()
    list = {}
    i = 0
    for item in department_info_group:
        count = countStaff(item.department_id)
        list.update({
            i: {
                "id": item.department_id,
                "name": item.department_name,
                "staff_count": count,
                'notice': item.notice,
                'clock_in_start': item.clock_in_start.isoformat(timespec='auto') if type(
                    item.clock_in_start) is datetime.time else '00:00:00',
                'clock_in_end': item.clock_in_end.isoformat(timespec='auto') if type(
                    item.clock_in_end) is datetime.time else '23:59:59',
                'clock_out_start': item.clock_out_start.isoformat(timespec='auto') if type(
                    item.clock_out_start) is datetime.time else '00:00:00',
                'clock_out_end': item.clock_out_end.isoformat(timespec='auto') if type(
                    item.clock_out_end) is datetime.time else '23:59:59'
            }
        })
        i += 1
    return list
