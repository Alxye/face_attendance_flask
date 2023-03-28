import random
from datetime import datetime, timedelta


# 随机生成一个真实的地址
def generate_address():
    addresses = [
        '江苏省苏州市工业园区星湖街218号',
        '江苏省苏州市吴中区越溪东路568号',
        '江苏省苏州市相城区黄畦路',
        '江苏省苏州市高新区金山路88号',
        '江苏省苏州市吴中区长桥街道科技园天平山路28号',
        '江苏省苏州市姑苏区阊门巷2号',
        '江苏省苏州市吴江区平望镇中环西路26号',
        '江苏省苏州市昆山市花园路158号',
        '江苏省苏州市常熟市虞山镇明珠北路58号',
        '江苏省苏州市张家港市临港新城金浦路9号',
        '江苏省苏州市太仓市城厢镇仓南路100号',
        '江苏省苏州市苏州工业园区星海街169号',
        '江苏省苏州市高新区玉山路88号',
        '江苏省苏州市吴中区越溪东路168号',
        '江苏省苏州市吴江区盛泽镇工业园区华夏路1号',
        '江苏省苏州市常熟市新区娄江路1100号',
        '江苏省苏州市太仓市浏河镇大润发购物广场',
        '江苏省苏州市张家港市沙洲镇南大街68号',
        '江苏省苏州市昆山市淀山湖镇绿地大道1111号',
        '江苏省苏州市吴中区城南路268号',
        '江苏省苏州市高新区星海街199号',
        '江苏省苏州市姑苏区苏州博物馆'
    ]
    return random.choice(addresses)

def static_address():
    addresses = [
        '江苏省苏州市苏州工业园区林泉街'
        '东南大学苏州研究院'
    ]
    return random.choice(addresses)


# 生成指定日期范围内的考勤数据
start_date_str = '2022-12-29'
end_date_str = '2023-03-30'
start_date = datetime.strptime(start_date_str, '%Y-%m-%d')
end_date = datetime.strptime(end_date_str, '%Y-%m-%d')
staff_id = 1116

date = start_date
while date <= end_date:
    # 随机生成上午和下午的考勤状态和地址
    am_type = random.choices([0, 1,  2], weights=[0.1, 0.8, 0.1])[0]
    pm_type = random.choices([0, 1,  2], weights=[0.1, 0.8, 0.1])[0]

    # am_type = random.randint(0, 2)
    # pm_type = random.randint(0, 2)
    am_address = static_address() if am_type != 0 else ''
    pm_address = static_address() if pm_type != 0 else ''

    # 随机生成上午和下午的打卡时间
    clock_in_time = date + timedelta(hours=random.randint(6, 10),
                                     minutes=random.randint(0, 59)) if am_type != 0 else None
    clock_out_time = date + timedelta(hours=random.randint(16, 20),
                                      minutes=random.randint(0, 59)) if pm_type != 0 else None

    # 构造 SQL 语句并打印出来
    sql = "INSERT INTO `wechat`.`attendance`(`staff_id`, `date`, `am_type`, `pm_type`"
    if am_type != 0:
        sql += ", `clock_in_time`, `am_address`"
    if pm_type != 0:
        sql += ", `clock_out_time`, `pm_address`"
    sql += ") VALUES ("
    sql += f"{staff_id}, '{date.strftime('%Y-%m-%d')}', {am_type}, {pm_type}"
    if am_type != 0:
        sql += f", '{clock_in_time}', '{am_address}'"
    if pm_type != 0:
        sql += f", '{clock_out_time}', '{pm_address}'"
    sql += ");"
    print(sql)

    # 将日期加 1 天
    date += timedelta(days=1)






