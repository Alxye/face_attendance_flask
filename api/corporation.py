from models.corporation import Corporation
from models.department import Department
from models.user import Users
from utils.data_process import Class_To_Data2

def GetAdminData():
    Admin_info_group =Users.query.filter(Users.type>=2).all()
    list = {}
    i = 0
    for item in Admin_info_group:
        list.update({
            i: {
                "id": i,
                "staff_id": item.staff_id,
                "type": item.type,
                "type_name": '管理员' if item.type==2 else '待审批管理员',
                "department_id": item.department_id,
                'department_name': Department.get(Department, item.department_id).department_name,
            }
        })
        i += 1
    return list

def Get():
    departmentInfo = Corporation.get(Corporation)
    if departmentInfo is None:
        return None
    else:
        info = Class_To_Data2(obj_list=departmentInfo, fields=Corporation.__fields__, type=1)
        return info


def GetName():
    departmentInfo = Corporation.get(Corporation)
    if departmentInfo is None:
        return ''
    else:
        return departmentInfo.name


def GetAddress():
    departmentInfo = Corporation.get(Corporation)
    if departmentInfo is None:
        return ''
    else:
        return departmentInfo.address


def GetNotice():
    departmentInfo = Corporation.get(Corporation)
    if departmentInfo is None:
        return ''
    else:
        return departmentInfo.notice


def Update(name, address, notice):
    corpInfo = Corporation.query.filter_by(id=1).first()
    if corpInfo is None:
        return False
    else:
        corpInfo.name = name
        corpInfo.address = address
        corpInfo.notice = notice
        Corporation.update(corpInfo)
        return True


def countStaff(flag=0):
    if flag == 0:
        count = Users.query.count()
    else:
        count = Users.query.filter_by(department_id=flag).count()
    return count


def getStaffDistribution():
    department_id_group = Department.query.all()
    list = {}
    i = 0
    for item in department_id_group:
        count = countStaff(item.department_id)
        list.update({
            i: {
                "name": item.department_name,
                "value": count
            }
        })
        i += 1
    print(list)
    return list
