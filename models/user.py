import datetime

from config import db_init as db
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash
import time

# 定义user模型类
class Users(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staff_id = db.Column(db.Integer, nullable=False)
    password = db.Column(db.String(45), nullable=False)
    name = db.Column(db.String(45), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    type = db.Column(db.Integer, nullable=False)
    reg_time = db.Column(db.DateTime, nullable=False)  # register time
    login_time = db.Column(db.Integer, nullable=False)  # register time
    department_id = db.Column(db.Integer,db.ForeignKey("department.department_id"), nullable=False)
    # face_info = db.Column(db.BLOB, nullable=False)
    openid = db.Column(db.String(255))
    face_info = db.Column(db.LargeBinary(16777216), nullable=False)

    def __repr__(self):
        return '<User %s>' % self.staff_id

    # 用于新建
    def __init__(self,staff_id, password='123456',department_id=0,type=0,name='new',age=0,reg_time='', openid='',face_info=None):
        self.staff_id = staff_id
        self.password = self.set_password(password)
        self.department_id = department_id
        self.name=name
        self.age=age
        self.reg_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.type = type
        self.openid = openid
        self.face_info = face_info
    # 用于注册用？
    # def __init__(self, staff_id, password):
    #     self.staff_id = staff_id
    #     self.password = password

    # @staticmethod
    # def update():
    #     try:
    #         db.session.commit()
    #     except SQLAlchemyError as e:
    #         db.session.rollback()
    #         reason = str(e)
    #         return reason

    # 将前端传来的明文 password转换为hash
    def set_password(self, password):
        return generate_password_hash(password)

    # 将前端传来的明文 password转化后的hash和数据库里的hash比较
    def check_password(self, hash, password):
        return check_password_hash(hash, password)

    # def check_password(self, db_password, submit_password):
    #     if db_password == submit_password:
    #         return True
    #     else:
    #         return False

    def get(self, staff_id):
        return self.query.filter_by(staff_id=staff_id).first()

    def add(self, user):
        db.session.add(user)
        return session_commit()

    def update(self):
        return session_commit()

    def delete(self, staff_id):
        self.query.filter_by(staff_id=staff_id).delete()
        return session_commit()


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason
