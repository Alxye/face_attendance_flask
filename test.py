# coding:utf8
from flask import Flask, request, render_template
import pymysql as mysql
import json

# con = mysql.connect(host='172.29.3.36', port=3306, user='root', password='123456', db="wechat")
con = mysql.connect(host='101.132.152.202', port=3306, user='root', password='123456', db="wechat")
print(con)
con.ping(True)
con.autocommit(True)
cur = con.cursor()

app = Flask(__name__)  # 新建app


@app.route('/')  # 设置路由
def index():  # 设置路由对应的函数
    return render_template("index.html")


@app.route("/userlist")
def userlist():
    sql = "select * from userlist"
    cur.execute(sql)
    data = cur.fetchall()
    dump_data = json.dumps(data)
    print(dump_data)
    return dump_data


@app.route('/delete')
def delete():
    name = request.args.get("name")
    print(name)
    sql = 'delete from userlist where name="%s"' % (name)
    print(sql)
    cur.execute(sql)
    return "ok"


@app.route('/add')
def add():
    name = request.args.get('name')
    age = request.args.get('age')
    sql = 'insert into userlist ( name , age ) values("%s","%s")' % (name, age)
    print(sql)
    cur.execute(sql)
    return "ok"


@app.route('/edit')
def edit():
    name = request.args.get('name');
    age = request.args.get('age')
    sql = 'update userlist set age=%s where name="%s"' % (age, name)
    print(sql)
    cur.execute(sql)
    return "ok"


@app.route('/chartdata')
def chartdata():
    sql = "select * from userlist"
    cur.execute(sql)
    dic = {}
    rest = {
        'title': [],
        'data': []
    }
    for d in cur.fetchall():
        age = d[1]  #
        dic[age] = dic.get(age, 0) + 1  # get如果有返回values否则返回0  把年龄和出现的次数放到一个字典中  eg:{23：5}   23 出现了5次
    for age, num in dic.items():
        rest['title'].append("%s" % (age))
        rest['data'].append(
            {'name': "%s" % (age), 'value': "%s" % num}

        )
    print(rest)
    return json.dumps(rest)  # 通过json向前端传输数据


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
