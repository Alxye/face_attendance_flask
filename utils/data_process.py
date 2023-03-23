# 数据模型类===》普通字典
#    user/[user,user,user]    属性清单,
#            数据源            数据模型类属性    0 obj / 1

import datetime

# zxx
def Class_To_Data2(obj_list, fields, type=0):
    """
    This function make multi/single obj to list.

    :param obj_list: object content
    :param fields: list index fields
    :param type: 0 -> multi object (Default); 1 -> single object
    :return: list
    """
    if not type:  # [obj,obj,obj.....]
        user_list = []
        for u in obj_list:
            temp = {}
            for f in fields:
                if f in ['create_time', 'login_time']:
                    temp[f] = datetime.datetime.strftime(getattr(u, f), "%Y-%m-%d %H:%M:%S ")
                else:
                    temp[f] = getattr(u, f)
            user_list.append(temp)
    else:  # obj
        user_list = {}
        for f in fields:
            if f in ['create_time', 'login_time']:
                d = getattr(obj_list, f)
                if d:
                    user_list[f] = datetime.datetime.strftime(d, "%Y-%m-%d %H:%M:%S ")
            else:
                user_list[f] = getattr(obj_list, f)
    return user_list


# tyz
def Class_To_Data(data_list,fields,type=0):
    if not type:  # [obj,obj]
        user_list = []
        for u in data_list:
            temp = {}
            for f in fields:
                if f in ['reg_time','login_time','clock_in_time','clock_out_time']:
                    temp[f] = datetime.datetime.strftime(getattr(u,f), "%Y-%m-%d %H:%M:%S ") if getattr(u,f) is not None else ''
                elif f in ['date']:
                    temp[f] = datetime.date.strftime(getattr(u,f), "%Y-%m-%d ")if getattr(u,f)is not None else ''
                elif f in ['clock_in_time','clock_out_time']:
                    temp[f] = datetime.time.strftime(getattr(u, f), "%H:%M:%S")if getattr(u,f) is not None else ''
                else:
                    temp[f] = getattr(u,f)
            user_list.append(temp)

    else:  # obj
        user_list = {}
        for f in fields:
            if f in ['reg_time', 'login_time','clock_in_time','clock_out_time']:
                d = getattr(data_list, f)
                if d:
                    user_list[f] = datetime.datetime.strftime(d, "%Y-%m-%d %H:%M:%S ")if d is not None else ''
            elif f in ['date']:
                user_list[f] = datetime.date.strftime(getattr(data_list, f), "%Y-%m-%d ")if getattr(data_list,f) is not None else ''
            elif f in ['clock_in_time', 'clock_out_time']:
                user_list[f] = datetime.time.strftime(getattr(data_list, f), "%H:%M:%S")if getattr(data_list,f) is not None else ''
            else:
                user_list[f] = getattr(data_list, f)

    return user_list
