# from models.user import Users
# from utils import db_commit
#
#
# # 类
# class User_operation:
#     def __init__(self):
#         self.__fields__ = ['id', 'staff_id', 'password', 'name', 'age', 'department_id', 'type', 'reg_time',
#                            'login_time',
#                            'face_info']
#
#     @staticmethod
#     def _all(self):
#         user_list = Users.query.all()
#         return user_list
#
#     @staticmethod
#     def _login(staff_id: int):
#         user_info = Users.query.filter_by(staff_id=int(staff_id), type=3).one_or_none()
#         return user_info
#
#     @staticmethod
#     def _update():
#         User.login_time
#         Users.update()

from models.user import Users


# class
class User_opration():
    def __init__(self):
        self.__fields__ = ['id', 'name', 'age', 'staff_id', 'type', 'reg_time', 'login_time', 'password',
                           'department_id', 'openid', 'face_info']
        # self.__fields__ = ['id', 'staff_id', 'password','department_id']


    def login(self, name, pwd):
        user_list = Users.query.filter_by(staff_id=name).first()
        print(user_list)
        return user_list

    def _reg(self, username, staffID, departmentID, openid, face_info):
        return Users(name=username, staff_id=staffID, department_id=departmentID, openid=openid, type=0, face_info = face_info)

    def _search_openid(self, openid):
        user_list = Users.query.filter_by(openid=openid).first()
        return user_list

    def _all(self):
        user_list = Users.query.all()
        return user_list

    def _id_check(self, staffID):
        user_list = Users.query.filter_by(staff_id=staffID).first()
        return user_list

    def _id_faceinfo(self, staffID):
        user_list = Users.query.filter_by(staff_id=staffID).first().face_info
        return user_list