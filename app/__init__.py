# -*- codeing = utf-8 -*-
# @Time : 2021/2/10 13:59
# @Author :王小刚
# @File :__init__.py.py
# @Software：PyCharm
from config import Config  # 从config模块导入Config类
from flask import Flask

app = Flask(__name__)
app.config.from_object(Config)
from app import routes