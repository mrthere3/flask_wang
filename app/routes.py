# -*- codeing = utf-8 -*-
# @Time : 2021/2/10 14:05
# @Author :王小刚
# @File :routes.py
# @Software：PyCharm
from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello ,World"
