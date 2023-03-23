from config import app
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor
import datetime
from api.user import *
from api.attendance import *
from config import db_init as db
import urllib
import json

info_list = []

def getYesterday():
    today=datetime.date.today()
    oneday=datetime.timedelta(days=1)
    yesterday=today-oneday
    return yesterday

def job():
    with app.app_context():
        data = datetime.date.today()
        user_list = User_search_all()
        for i in user_list:
            staffid = i.staffID
            record = Attendance_auto_insert(staffid,data)
            db.session.add(record)
        db.session.commit()
        for i in user_list:
            app.scheduler.remove_job(i)
    print('Job done')

def job_message(serverToken, data):
    # 要请求的微信API
    url = 'https://api.weixin.qq.com/cgi-bin/message/subscribe/send?access_token={serverToken}'.format(
        serverToken=serverToken)
    # 数据格式化(从这里开始对上面的data进行格式化,转成符合post的json参数形式)
    data = json.dumps(data)
    # 数据格式化
    data = bytes(data, 'utf8')
    # 数据格式化
    request1 = urllib.request.Request(url)
    # post服务器请求
    result = urllib.request.urlopen(request1, data).read()
    # 打印结果
    # print(result)

def add_message_longtime(serverToken, data, time_, openid):
    app.scheduler.add_job(job_message, trigger='cron', args=[serverToken, data], day_of_week='1-5',
                          hour=int(str(time_).split(':')[0]), minute=int(str(time_).split(':')[1]),
                          second=int(str(time_).split(':')[2]),id=openid)
    info_list.append(openid)
    app.scheduler.print_jobs()

def add_message(serverToken, data, time_, date_, openid):
    app.scheduler.add_job(job_message, trigger='date', args=[serverToken, data], run_date=f'{str(date_)} {str(time_)}', id=openid)
    # app.scheduler.print_jobs()

def remove_message(openid):
    app.scheduler.print_jobs()
    if openid in info_list:
        app.scheduler.remove_job(openid)
        info_list.remove(openid)
        # print('job clear')

def search_state(openid):
    # print(info_list)
    if openid in info_list:
        return 1
    else:
        return 0


# def job2(): #refresh all user attendance records
#     with app.app_context():
#         yesterday = getYesterday()
#         user_list = User_search_all()
#         for i in user_list:
#             staffid = i.staffID
#             record = Attendance_auto_insert(staffid,yesterday)
#             change = 0
#             if(record.am_type==0):
#                 record.am_type = 2
#                 change = 1
#             if(record.pm_type==0):
#                 record.pm_type = 2
#                 change = 1
#             if(change==1):
#                 db.session.add(record)
#         db.session.commit()
#     print('Job2 done')

# 1.定义执行器a
exeutors = {
    "default":ProcessPoolExecutor(max_workers=10)
}
app.scheduler = BackgroundScheduler(exeutors=exeutors)


app.scheduler.add_job(job, trigger='cron', day_of_week='1-5', hour=0, minute=0, second=0)

# app.scheduler.add_job(job2, trigger='cron', day_of_week='2-6', hour=0, minute=0, second=0)


