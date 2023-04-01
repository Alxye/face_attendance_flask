<h1 align="center">智慧考勤管理 - 后端服务</h1>
<p align="center">
    <a href="https://www.bilibili.com/video/BV1mh41137yS/?vd_source=9a233e677646447199a2bcdb7c74c126">
        Demo视频
    </a>
</p>
基于人脸识别与定位的智慧考勤系统<br>
该仓库用于人脸考勤系统后端代码开发，技术：flask、faceNet、MtCNN

```                                                            mysql=====>sql
flask ---> pymysql库--> sqlalchemy（ORM）==>flask_sqlalchemy ===>面向对象方式操作数据
```
## 基本环境
- Linux：Ubuntu 20.04 64位
- Python：Python 3.8.10
- MySQL：8.0.32 - 0ubuntu0.20.04.2 for Linux on x86_64 ((Ubuntu))
## 代码文件结构说明：
| 文件/文件夹            | 说明               |
|-------------------|------------------|
| AI_models         | 人脸模型实现类          |
| models            | 模型类              |
| operation         | 调用模型类数据库         |
| api               | 一系列方法：业务逻辑 数据封装  |
| routes            | 路由配置 request     |
| utils             | 工具类 对象转list、用户验证 |
| static            | 存放资源，人脸          |
| app.py            |                  |
| config.py         | 配置文件             |
| my_trigger.py     |                  |
| WXBizDataCrypt.py |                  |
| requirement.txt   | 环境要求             |
| wechat.sql        | 数据库结构文件          |
## 代码部署说明

部署该仓库，请将AI模型文件 `model_resnet34_triplet.pt` 放入 `AI_model\facenet\weights` 文件夹下

- 1、模型下载
    - 国内：链接：https://pan.baidu.com/s/1PROYJ0o7Lco3uFcdUBEONw?pwd=7cgk 提取码：7cgk
    - 国际：https://drive.google.com/file/d/1kdeI8wkH6UfpznlIvIpjaixfbE2WQhSV/view?usp=share_link
- 2、config文件自定义
    - 在appID、appSecret、template_id更换微信小程序开发者相关的信息
    - 修改数据库配置
        - HostName：主机名，若数据库在本机则默认localhost，若为远程数据库，需变更为主机公网ip
        - Port：默认3306端口，指链接数据库端口
        - UserName：连接数据库用户名，默认root
        - Password：连接数据库密码
        - DataBase：连接的数据库
- 3、app文件运行配置 `app.run(host='0.0.0.0', port=5002, debug=True)`
  - 本地运行，请修改host为本机地址或127.0.0.1
  - 远程服务器默认使用0.0.0.0，达到公网访问的目的
  - 公网访问port需开启5002端口
  - debug=True开启热更新模式
## 生产环境配置说明
部署Flask应用到生产环境，需在服务器端构建nginx与gunicorn配合使用
### 1、准备
- Linux机器一台，包括但不限于，VPS，本地虚拟机，实体服务器、云服务器等
- 网络
- 连接Linux服务器的工具（MobaXterm，xshell等）
### 2、安装基本环境
- 虚拟环境  
虚拟环境可以搭建独立的python运行环境, 使得单个项目的运行环境与其它项目互不影响
  ```angular2html
  # 安装
  sudo pip install virtualenv
  sudo pip install virtualenvwrapper
    
  # 创建目录用来存放虚拟环境
  # 此命令将虚拟环境安装在当前目录
  virtualenv -p python3 xxxxx(虚拟环境名字  
    
  # 激活虚拟环境
  source (目录)/xxxxx/bin/activate
    
  # 退出虚拟环境
  deactivate
  ```
- 安装本地requirement文件
  - 1. 激活环境
  - 2. 终端命令 `pip install -r (路径) /requirements.txt`
- 全局环境安装requirement文件
  - 终端命令 `pip install -r (路径) /requirements.txt`

![Image](https://github.com/Alxye/face_attendance_flask/raw/main/static/env-setup.png)
### 3、 nginx配置
- 安装nginx
- 对nginx进行配置，配置文件一般在`/etc/nginx/sites-available/default`
- 先对原文件进行备份,终端执行  
`cp /etc/nginx/sites-available/default default.bak`<br/>
- 再修改,终端执行  
`sudo vi /etc/nginx/sites-available/default`<br/>
其中 `/home/project/dist` 为项目vue3构建的网页目录
  ```angular2html
  server {
      listen 80 default_server;
      listen [::]:80 default_server;
    
      root /home/project/dist;
    
      # Add index.php to the list if you are using PHP
      index index.html index.htm index.nginx-debian.html;
    
      server_name 101.132.152.202;
  }    
  ```
### 4、 gunicorn配置
- 安装gunicorn
  - 在全局环境下，在Flask根目录执行命令：`gunicorn -w 2 -b 0.0.0.0:5002 app:app`
  - 在虚拟环境下，激活虚拟环境在Flask根目录执行命令：`(虚拟环境目录)/bin/gunicorn -w 2 -b 0.0.0.0:5002 app:app`


![Image](https://github.com/Alxye/face_attendance_flask/raw/main/static/gunicorn-exp.png)
- 为gunicorn启动全局自启动服务  
`创建："/etc/systemd/system/gunicorn.service"`
```
[Unit]
# 描述
Description=gunicorn for vue3
# 在网络服务启动后再启动
After=network.target

[Service]
User=root
# 项目文件目录
WorkingDirectory=/home/project/flask
# gunicorn启动命令:gunicorn 全局安装   则不需要激活特定环境
# gunicorn启动命令:gunicorn 非全局安装 需要激活特定环境 
# ExecStart=(虚拟环境目录)/bin/gunicorn -w 2 -b 0.0.0.0:5002 app:app
ExecStart=gunicorn -w 2 -b 0.0.0.0:5002 app:app
# 错误重启
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
`终端命令`
```
# 重新加载配置文件
sudo systemctl daemon-reload
# 开启服务
sudo systemctl start gunicorn.service
# 查看服务状态
sudo systemctl status gunicorn.service
# 设置开机启动
sudo systemctl enable gunicorn.service
```
若部署成功，网页输入 http:// 自己的服务器ip /  (http://101.132.152.202/ 将会重定位到 http://101.132.152.202/#/login)

![Image](https://github.com/Alxye/face_attendance_flask/raw/main/static/success.png)
