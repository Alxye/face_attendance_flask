from config import db_init as db
from sqlalchemy.exc import SQLAlchemyError


# 定义数据库提交
def db_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason
