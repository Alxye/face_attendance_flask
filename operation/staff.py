import datetime

from flask import jsonify

# from db_config import db
from config import db_init as db
from models.user import Users


# class
class staff_opration():
    def __init__(self):
        self.__fields__ = ['staff_id', 'name', 'age', 'type', 'department_id', 'reg_time']

    def _all(self, i, s, id, did):
        if id:
            # query.join(department,staffs.department_id==department.department_id)
            # staff_list = Users.query.filter_by(staff_id=id,department_id=did).offset((i-1)*s).limit(s).all()
            staff_list = Users.query.filter(Users.type <= 1, Users.staff_id == id, Users.department_id == did).offset(
                (i - 1) * s).limit(s).all()
        else:
            # staff_list = Users.query.filter_by(department_id=did).offset((i - 1) * s).limit(s).all()
            staff_list = Users.query.filter(Users.type <= 1, Users.department_id == did).offset((i - 1) * s).limit(
                s).all()
        return staff_list

    def get_by_staff_id(self, staff_id):
        staff_list = Users.query.filter(Users.staff_id == staff_id).all()
        return staff_list

    def create(self, staff_id, name='new', age=0, department_id=0, type=0):
        example = Users(staff_id=staff_id, name=name, age=age, department_id=department_id, type=type,
                        reg_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        db.session.add(example)
        db.session.commit()
        return "1";

    def update(self, staff_id, name, age, department_id, type):
        res = Users.query.filter_by(staff_id=staff_id).update(
            {"name": name, "age": age, "department_id": department_id, "type": type})
        db.session.commit()
        return jsonify(res)

    def delete(self, id):
        res = Users.query.filter_by(staff_id=id).delete()
        db.session.commit()
        return jsonify(res)

    def login(self, name, pwd):
        user_list = Users.query.filter_by(username=name).first()
        print(user_list)
        return user_list

    def get_total_number(self, did):
        return db.session.query(Users).filter().count()

    def get_total_number_by_department(self, did):
        return db.session.query(Users).filter(Users.type <= 1, Users.department_id == did).count()

    def get_did(self, name):
        return db.session.query(Users.department_id).filter_by(staff_id=name).all()
