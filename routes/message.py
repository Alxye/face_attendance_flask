from flask import Blueprint,request
message = Blueprint('message',__name__)
import json,requests
from api.department import *
import urllib
import datetime
from my_trigger import add_message,remove_message,search_state,add_message_longtime
from config import *


@message.route('/subscription',methods=['GET','POST'])
def message_subscription():
    if request.method == 'POST':
        now = datetime.datetime.now()
        departmentid = int(request.json.get('departmentid'))
        openid = request.json.get('openid')
        time1,time2,time3,time4 = Query_department_attendance_time2(departmentid)
        data1 = {
            # 用户的openId
            "touser": openid,
            # 订阅消息模板id
            "template_id":template_id,
            # 要跳转的页面
            "page": "pages/main/main",
            "miniprogram_state": 'trial',
            # 模板消息对应的内容设置
            "data": {
                # "thing1": {
                #     "value": "签到提醒"
                # },
                # "thing2": {
                #     "value": "点击进入小程序签到"
                # },
                # "time15": {
                #     "value": str(time1)
                # },
                # "time13": {
                #     "value": str(time2)
                # }
                "time2": {
                    "value": str(time1)
                },
                "thing6": {
                    "value": '今日还未考勤，请立即安排'
                },
                "thing8": {
                    "value": '考勤签到'
                },
                "thing9": {
                    "value": '您有新的考勤计划，请查看签到'
                }
            }
        }
        data2 = {
            # 用户的openId
            "touser": openid,
            # 订阅消息模板id
            "template_id": template_id,
            # 要跳转的页面
            "page": "pages/main/main",
            "miniprogram_state": 'trial',
            # 模板消息对应的内容设置
            "data": {
                # "thing1": {
                #     "value": "签到提醒"
                # },
                # "thing2": {
                #     "value": "点击进入小程序签到"
                # },
                # "time15": {
                #     "value": str(time3)
                # },
                # "time13": {
                #     "value": str(time4)
                # }
                "time2": {
                    "value": str(time3)
                },
                "thing6": {
                    "value": '今日还未考勤，请立即安排'
                },
                "thing8": {
                    "value": '考勤签到'
                },
                "thing9": {
                    "value": '您有新的考勤计划，请查看签到'
                }
            }
        }
        # 服务端token
        wx_access_api = "https://api.weixin.qq.com/cgi-bin/token" + "?grant_type=client_credential" + "&appid=" + appID + "&secret=" + appSecret
        response_data = requests.get(wx_access_api)
        resData = response_data.json()
        serverToken = resData['access_token']
        add_message(serverToken, data1, time1, now.date(), openid+f'_1_{now.date()}')
        add_message(serverToken, data2, time3, now.date(), openid+f'_2_{now.date()}')

        return {
            'code': 1
        }

@message.route('/subscription_longtime',methods=['GET','POST'])
def message_subscription_longtime():
    if request.method == 'POST':
        now = datetime.datetime.now()
        departmentid = int(request.json.get('departmentid'))
        openid = request.json.get('openid')
        time1,time2,time3,time4 = Query_department_attendance_time2(departmentid)
        data1 = {
            # 用户的openId
            "touser": openid,
            # 订阅消息模板id
            "template_id":template_id,
            # 要跳转的页面
            "page": "pages/main/main",
            "miniprogram_state": 'trial',
            # 模板消息对应的内容设置
            "data": {
                # "thing1": {
                #     "value": "签到提醒"
                # },
                # "thing2": {
                #     "value": "点击进入小程序签到"
                # },
                # "time15": {
                #     "value": str(time1)
                # },
                # "time13": {
                #     "value": str(time2)
                # }
                "time2": {
                    "value": str(time1)
                },
                "thing6": {
                    "value": '今日还未考勤，请立即安排'
                },
                "thing8": {
                    "value": '考勤签到'
                },
                "thing9": {
                    "value": '您有新的考勤计划，请查看签到'
                }
            }
        }
        data2 = {
            # 用户的openId
            "touser": openid,
            # 订阅消息模板id
            "template_id": template_id,
            # 要跳转的页面
            "page": "pages/main/main",
            "miniprogram_state": 'trial',
            # 模板消息对应的内容设置
            "data": {
                # "thing1": {
                #     "value": "签到提醒"
                # },
                # "thing2": {
                #     "value": "点击进入小程序签到"
                # },
                # "time15": {
                #     "value": str(time3)
                # },
                # "time13": {
                #     "value": str(time4)
                # }
                "time2": {
                    "value": str(time3)
                },
                "thing6": {
                    "value": '今日还未考勤，请立即安排'
                },
                "thing8": {
                    "value": '考勤签到'
                },
                "thing9": {
                    "value": '您有新的考勤计划，请查看签到'
                }
            }
        }
        # 服务端token
        wx_access_api = "https://api.weixin.qq.com/cgi-bin/token" + "?grant_type=client_credential" + "&appid=" + appID + "&secret=" + appSecret
        response_data = requests.get(wx_access_api)
        resData = response_data.json()
        serverToken = resData['access_token']
        add_message_longtime(serverToken, data1, time1, openid+'_1')
        add_message_longtime(serverToken, data2, time3, openid+'_2')

        return {
            'code': 1
        }

@message.route('/cancel_subscription',methods=['GET','POST'])
def message_cancel_subscription():
    if request.method == 'POST':
        openid = request.json.get('openid')
        remove_message(openid+'_1')
        remove_message(openid+'_2')

        return {
            'code': 1
        }

@message.route('/subscription_state_search',methods=['GET','POST'])
def message_subscription_state_search():
    if request.method == 'POST':
        openid = request.json.get('openid')
        if(search_state(openid+'_1')):
            res = {
                'code': 1
            }
        else:
            res = {
                'code': 0
            }
        return res