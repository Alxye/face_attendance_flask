
# from db_config import db
from config import db_init as db
# 定义staffs模型类
class Attendance(db.Model):
    __tablename__ = 'attendance'
    staff_id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, primary_key=True)
    salary = db.Column(db.Float)
    am_type = db.Column(db.Integer)
    pm_type = db.Column(db.Integer)
    am_address = db.Column(db.String(255))
    pm_address = db.Column(db.String(255))
    clock_in_time = db.Column(db.DateTime,nullable=True)
    clock_out_time = db.Column(db.DateTime,nullable=True)


    def __repr__(self):
        return '<attendance %s %d>' % self.date, self.staff_id

