from config import db_init as db
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash


# 定义Department模型类
class Department(db.Model):
    __tablename__ = 'department'
    __fields__ = ['department_id',
                  'department_name',
                  'notice',
                  'clock_in_start',
                  'clock_out_start',
                  'clock_in_end',
                  'clock_out_end']
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String(45), nullable=False)
    notice = db.Column(db.String(45), nullable=False)
    clock_in_start = db.Column(db.Time, nullable=False)
    clock_out_start = db.Column(db.Time, nullable=False)
    clock_in_end = db.Column(db.Time, nullable=False)
    clock_out_end = db.Column(db.Time, nullable=False)

    def __repr__(self):
        return '<Department %s>' % self.department_id

    # 用于新建新部门用？
    def __init__(self, department_name, notice):
        self.department_name = department_name
        self.notice = notice

    # def set_password(self, password):
    #     return generate_password_hash(password)

    # def check_password(self, hash, password):
    #     return check_password_hash(hash, password)

    # def check_password(self, db_password, submit_password):
    #     print(db_password)
    #     print(submit_password)
    #     if db_password == submit_password:
    #         return True
    #     else:
    #         return False

    def get(self, department_id):
        return self.query.filter_by(department_id=department_id).first()

    def findWithName(self, department_name):
        return self.query.filter_by(department_name=department_name).first()


    def add(self, department):
        db.session.add(department)
        return session_commit()

    def update(self):
        return session_commit()

    def delete(self, department_id):
        self.query.filter_by(department_id=department_id).delete()
        return session_commit()


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason
