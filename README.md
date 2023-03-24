# face_attendance_flask
该仓库用于人脸考勤系统后端代码开发，flask
```                                                            mysql=====>sql
flask ---> pymysql库--> sqlalchemy（ORM）==>flask_sqlalchemy ===>面向对象方式操作数据
```
## 代码文件结构说明：
- models     模型类
- operation  调用模型类数据库
- api        一系列方法：业务逻辑    数据封装
- routes     路由配置   request  retu
- app.py
## 代码部署说明
部署该仓库，请将AI模型文件 `model_resnet34_triplet.pt` 放入 `AI_model\facenet\weights` 文件夹下
- 模型下载
  - 国内：链接：https://pan.baidu.com/s/1PROYJ0o7Lco3uFcdUBEONw?pwd=7cgk 提取码：7cgk 
  - 国际：https://drive.google.com/file/d/1kdeI8wkH6UfpznlIvIpjaixfbE2WQhSV/view?usp=share_link
## editing!