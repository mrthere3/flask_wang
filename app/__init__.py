# -*- codeing = utf-8 -*-
# @Time : 2021/2/10 13:59
# @Author :王小刚
# @File :__init__.py.py
# @Software：PyCharm
from flask import Flask
from config import Config#从config模块导入Config类
from flask_login import LoginManager
from flask_bootstrap import Bootstrap

from flask_sqlalchemy import SQLAlchemy#从包中导入类
from flask_migrate import Migrate
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)


db = SQLAlchemy(app)#数据库对象
migrate = Migrate(app, db)#迁移引擎对象
login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)
bootstrap = Bootstrap(app)

from app import routes,models#导入一个新模块models，它将定义数据库的结构，目前为止尚未编写
