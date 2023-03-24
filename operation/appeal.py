import datetime
import json

from flask import jsonify

# from db_config import db
from config import db_init as db
# from models.appeal import appeal
from models.attendance_appeal import AttendanceAppeal
from models.user import Users


# class
class appeal_opration():
    def __init__(self):
        self.__fields__ = ['staff_id', 'id', 'date', 'state', 'appeal_reason','reject_reason','category','time_state']

    def _submit(self, date, staffID, appeal_reason, time_state, category):
        return AttendanceAppeal(date=date, staff_id=staffID, appeal_reason=appeal_reason, state=0, time_state=time_state,
                       category=category)

    def _all(self,i,s,id,did):
        # AttendanceAppeal.query.filter_by(state=0). \
        #     outerjoin(Users, AttendanceAppeal.staff_id == Users.staff_id). \
        #     add_entity(Users).filter(Users.department_id == department_id). \
        #     count()

        if id:
            # query.join(department,staffs.department_id==department.department_id)
            staff_list = AttendanceAppeal.query.filter_by(staff_id=id).order_by(AttendanceAppeal.state).offset((i - 1) * s).limit(s).all()
        else:
            staff_list = AttendanceAppeal.query.filter_by().\
                order_by(AttendanceAppeal.state).offset((i - 1) * s).limit(s).all()
        return staff_list

    def _all_by_department(self,i,s,id,did):
        # AttendanceAppeal.query.filter_by(state=0). \
        #     outerjoin(Users, AttendanceAppeal.staff_id == Users.staff_id). \
        #     add_entity(Users).filter(Users.department_id == department_id). \
        #     count()

        if id:
            # query.join(department,staffs.department_id==department.department_id)
            # staff_list = AttendanceAppeal.query.filter_by(staff_id=id).order_by(AttendanceAppeal.state).offset((i - 1) * s).limit(s).all()
            staff_list = AttendanceAppeal.query. \
                outerjoin(Users, AttendanceAppeal.staff_id == Users.staff_id). \
                add_entity(Users).filter(Users.department_id == did,Users.staff_id==id). \
                order_by(AttendanceAppeal.state).offset((i - 1) * s).limit(s).all()
        else:
            staff_list = AttendanceAppeal.query.\
                outerjoin(Users, AttendanceAppeal.staff_id == Users.staff_id). \
                add_entity(Users).filter(Users.department_id == did). \
                order_by(AttendanceAppeal.state).offset((i - 1) * s).limit(s).all()

        # s = json.dumps(staff_list, ensure_ascii=False, default=lambda obj: obj.__dict__)
        # print('1',type(staff_list))
        # print('2',type(staff_list[0]))
        # print('3',type(staff_list[0][0]))
        return staff_list

    def create(self,staff_id,state,appeal_reason,reject_reason,date):
        example = AttendanceAppeal(staff_id=staff_id,state=state, appeal_reason=appeal_reason,reject_reason=reject_reason,date=date)
        db.session.add(example)
        db.session.commit()
        return "1";

    def update(self,id,rej):
        if(rej==""):
            res = AttendanceAppeal.query.filter_by(id=id).update({"state":1})
        else:
            res=AttendanceAppeal.query.filter_by(id=id).update({"state":2,"reject_reason":rej})
        db.session.commit()
        return jsonify(res)

    def delete(self, id):
        res=AttendanceAppeal.query.filter_by(id=id).delete()
        db.session.commit()
        return jsonify(res)
    def get_total_number(self,did,id):
        #return db.session.query(AttendanceAppeal).filter().count()
        if id:
            query = db.session().query(AttendanceAppeal)
            query = query.join(Users, AttendanceAppeal.staff_id == Users.staff_id)
            staff_list = query.filter_by(staff_id=id, department_id=did).count()
            return staff_list
        else:
            query = db.session().query(AttendanceAppeal)
            query = query.join(Users, AttendanceAppeal.staff_id == Users.staff_id)
            staff_list = query.filter_by(department_id=did).count()
            print('shuliang', staff_list)
            return staff_list
