from config import db_init as db
from sqlalchemy.exc import SQLAlchemyError


# 定义Corporation模型类
class Corporation(db.Model):
    __tablename__ = 'corporation'
    __fields__ = ['id', 'name', 'notice', 'address']
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(45), autoincrement=True)
    notice = db.Column(db.String(45), nullable=False)
    address = db.Column(db.String(45), nullable=False)

    def __repr__(self):
        return '<Corporation %s>' % self.name

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

    def get(self):
        return self.query.filter_by(id=1).first()

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
