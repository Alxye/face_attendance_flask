import datetime

from flask import jsonify
from sqlalchemy import extract

from config import db_init as db
# from db_config import db
from models.attendance import Attendance as attendance
# from models.staff import staffs
from models.user import Users

import calendar

# class
class attendance_opration():
    def __init__(self):
        # self.__fields__ = ['staff_id', 'date', 'salary', 'am_type', 'pm_type', 'clock_in_time', 'clock_out_time']
        self.__fields__ = ['clock_in_time', 'clock_out_time', 'am_type', 'pm_type', 'am_address', 'pm_address', 'salary',
                       'staff_id', 'date']
    # wechat-----------
    def _search_today_record(self, staffID, date):
        return attendance.query.filter_by(staff_id=staffID, date=date).first()

    def _insert_today_record(self, am_type, pm_type, staffID, date):
        return attendance(am_type=am_type, pm_type=pm_type, am_address="", pm_address="", salary=0.0, staff_id=staffID,
                          date=date)

    def _auto_insert_record(self, staffID, date):
        return attendance(am_type=0, pm_type=0, am_address="", pm_address="", salary=0.0, staff_id=staffID,
                          date=date)
    # wechat-----------


    def _all(self, i, s, id, date, did):
        if date:
            if id:
                query = db.session().query(attendance).filter_by(date=date)
                query = query.join(Users, attendance.staff_id == Users.staff_id)
                staff_list = query.filter_by(staff_id=id, department_id=did).offset((i - 1) * s).limit(s).all()
            else:
                query = db.session().query(attendance).filter_by(date=date)
                query = query.join(Users, attendance.staff_id == Users.staff_id)
                staff_list = query.filter_by(department_id=did).offset((i - 1) * s).limit(s).all()
        else:
            if id:
                # staff_list = attendance.query.filter_by(staff_id=id).offset((i - 1) * s).limit(s).all()
                query = db.session().query(attendance)
                query = query.join(Users, attendance.staff_id == Users.staff_id)
                staff_list = query.filter_by(staff_id=id, department_id=did).offset((i - 1) * s).limit(s).all()
            else:
                query = db.session().query(attendance)
                query = query.join(Users, attendance.staff_id == Users.staff_id)
                staff_list = query.filter_by(department_id=did).offset((i - 1) * s).limit(s).all()
        # print(staff_list)
        return staff_list

    def create(self, staff_id, date, am_type, pm_type, clock_in_time, clock_out_time):
        example = attendance(staff_id=staff_id, date=date, am_type=am_type, pm_type=pm_type,
                             clock_in_time=clock_in_time, clock_out_time=clock_out_time)
        db.session.add(example)
        db.session.commit()
        return "1";

    def create_attendance(self, staff_id, date, am_type, pm_type):
        example = attendance(staff_id=staff_id, date=date, am_type=am_type, pm_type=pm_type)
        db.session.add(example)
        db.session.commit()
        return "1";

    def exist(self, staff_id, date):
        info = attendance.query.filter_by(staff_id=staff_id, date=date).all()
        if info == []:
            return False
        else:
            return True

    def update(self, staff_id, date, am_type, pm_type, ic, oc):
        res = attendance.query.filter_by(staff_id=staff_id, date=date).update(
            {"clock_in_time": ic, "clock_out_time": oc, "am_type": am_type, "pm_type": pm_type})
        db.session.commit()
        return jsonify(res)

    def update_amclock_state(self, staff_id, date, am_type):
        res = attendance.query.filter_by(staff_id=staff_id, date=date).update({"am_type": am_type})
        db.session.commit()
        return jsonify(res)

    def update_pmclock_state(self, staff_id, date, pm_type):
        res = attendance.query.filter_by(staff_id=staff_id, date=date).update({"pm_type": pm_type})
        db.session.commit()
        return jsonify(res)

    def delete(self, id, date):
        res = attendance.query.filter_by(staff_id=id, date=date).delete()
        db.session.commit()
        return jsonify(res)

    def get_total_number(self, did,id,date):
        if date:
            if id:
                query = db.session().query(attendance).filter_by(date=date)
                query = query.join(Users, attendance.staff_id == Users.staff_id)
                staff_list = query.filter_by(staff_id=id, department_id=did).count()
                return staff_list
            else:
                query = db.session().query(attendance).filter_by(date=date)
                query = query.join(Users, attendance.staff_id == Users.staff_id)
                staff_list = query.filter_by(department_id=did).count()
                print('shuliang', staff_list)
                return staff_list
        else:
            if id:
                query = db.session().query(attendance)
                query = query.join(Users, attendance.staff_id == Users.staff_id)
                staff_list = query.filter_by(staff_id=id, department_id=did).count()
                return staff_list
            else:
                query = db.session().query(attendance)
                query = query.join(Users, attendance.staff_id == Users.staff_id)
                staff_list = query.filter_by(department_id=did).count()
                print('shuliang', staff_list)
                return staff_list


    def get_attendanceByMonth(self, did):
        now = datetime.datetime.now()
        today_year = now.year
        last_year = int(now.year) - 1
        today_year_months = range(1, now.month)
        # 得到去年的每个月的时间  last_year_months 等于10 11 12
        data = []
        for i in range(now.month, 13):
            d = db.session.query(attendance).filter(extract('month', attendance.date) == i,
                                                    extract('year', attendance.date) == last_year).count()
            data.append(d)
        for i in range(1, now.month):
            d = db.session.query(attendance).filter(extract('month', attendance.date) == i,
                                                    extract('year', attendance.date) == now.year).count()
            data.append(d)

        return data

    def get_attendanceByDay(self, did):
        now = datetime.datetime.now()
        today_year_months = range(1, now.month)
        data = []

        for i in range(1, now.day):
            query = db.session().query(attendance)
            query = query.join(Users, attendance.staff_id == Users.staff_id)
            d = query.filter(extract('day', attendance.date) == i, extract('month', attendance.date) == now.month,
                             extract('year', attendance.date) == now.year, Users.department_id == did).count()
            data.append(d)
        for i in range(now.day, 31):
            data.append(0)

        return data

    def get_checkinByDay(self, did,month):
        now = month
        # now = datetime.datetime.now()
        today_year_months = range(1, now.month)
        data = []
        monthRange = calendar.monthrange(now.year, now.month)
        print(monthRange)
        for i in range(1, monthRange[1]+1):
            query = db.session().query(attendance)
            query = query.join(Users, attendance.staff_id == Users.staff_id)
            d = query.filter(attendance.am_type == 1, extract('day', attendance.date) == i,
                             extract('month', attendance.date) == now.month,
                             extract('year', attendance.date) == now.year, Users.department_id == did).count()
            data.append(d)
        # for i in range(now.day, 31):
        #     data.append(0)

        return data

    def get_checkinByDay0(self, did,month):
        now = month
        # now = datetime.datetime.now()
        today_year_months = range(1, now.month)
        data = []
        monthRange = calendar.monthrange(now.year, now.month)
        print(monthRange)
        for i in range(1, monthRange[1]+1):
            query = db.session().query(attendance)
            query = query.join(Users, attendance.staff_id == Users.staff_id)
            d = query.filter(attendance.am_type == 0, extract('day', attendance.date) == i,
                             extract('month', attendance.date) == now.month,
                             extract('year', attendance.date) == now.year, Users.department_id == did).count()
            data.append(d)
        # for i in range(now.day, 31):
        #     data.append(0)

        return data

    def get_checkinByDay2(self, did,month):

        now = month
        # now = datetime.datetime.now()

        today_year_months = range(1, now.month)
        data = []
        monthRange = calendar.monthrange(now.year, now.month)
        print(monthRange)
        for i in range(1, monthRange[1]+1):
            query = db.session().query(attendance)
            query = query.join(Users, attendance.staff_id == Users.staff_id)
            d = query.filter(attendance.am_type == 2, extract('day', attendance.date) == i,
                             extract('month', attendance.date) == now.month,
                             extract('year', attendance.date) == now.year, Users.department_id == did).count()
            data.append(d)
        # for i in range(now.day, 31):
        #     data.append(0)

        return data

    def checkoutByDay1(self, did,month):
        now = month
        today_year_months = range(1, now.month)
        data = []
        monthRange = calendar.monthrange(now.year, now.month)
        print(monthRange)
        for i in range(1, monthRange[1] + 1):
        # for i in range(1, now.day):
            query = db.session().query(attendance)
            query = query.join(Users, attendance.staff_id == Users.staff_id)
            d = query.filter(attendance.pm_type == 1, extract('day', attendance.date) == i,
                             extract('month', attendance.date) == now.month,
                             extract('year', attendance.date) == now.year, Users.department_id == did).count()
            data.append(d)
        # for i in range(now.day, 31):
        #     data.append(0)

        return data

    def checkoutByDay0(self, did,month):
        now = month
        today_year_months = range(1, now.month)
        data = []
        monthRange = calendar.monthrange(now.year, now.month)
        print(monthRange)
        for i in range(1, monthRange[1] + 1):
            query = db.session().query(attendance)
            query = query.join(Users, attendance.staff_id == Users.staff_id)
            d = query.filter(attendance.pm_type == 0, extract('day', attendance.date) == i,
                             extract('month', attendance.date) == now.month,
                             extract('year', attendance.date) == now.year, Users.department_id == did).count()
            data.append(d)
        # for i in range(now.day, 31):
        #     data.append(0)

        return data

    def checkoutByDay2(self, did,month):
        now = month
        today_year_months = range(1, now.month)
        data = []
        monthRange = calendar.monthrange(now.year, now.month)
        print(monthRange)
        for i in range(1, monthRange[1] + 1):
            query = db.session().query(attendance)
            query = query.join(Users, attendance.staff_id == Users.staff_id)
            d = query.filter(attendance.pm_type == 2, extract('day', attendance.date) == i,
                             extract('month', attendance.date) == now.month,
                             extract('year', attendance.date) == now.year, Users.department_id == did).count()
            data.append(d)
        # for i in range(now.day, 31):
        #     data.append(0)

        return data

    def get_alldata(self, did, date):
        if date:
            query = db.session().query(attendance).filter_by(date=date)
            query = query.join(Users, attendance.staff_id == Users.staff_id)
            return query.filter(Users.department_id == did).all()
        else:
            query = db.session().query(attendance).filter_by()
            query = query.join(Users, attendance.staff_id == Users.staff_id)
            return query.filter(Users.department_id == did).all()
