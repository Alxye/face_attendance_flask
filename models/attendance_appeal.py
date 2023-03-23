from config import db_init as db
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash


# 定义user模型类
class AttendanceAppeal(db.Model):
    __tablename__ = 'attendance_appeal'

    time_state = db.Column(db.Integer)
    category = db.Column(db.Integer)

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    staff_id = db.Column(db.Integer, nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    appeal_reason = db.Column(db.String(45), nullable=False)
    state = db.Column(db.Integer, nullable=True)
    reject_reason = db.Column(db.String(45), nullable=False)

    # user = db.orm.relationship(User, backref=sa.orm.backref('other_thing', uselist=False))

    def __repr__(self):
        return '<AttendanceAppeal %s>' % self.id

