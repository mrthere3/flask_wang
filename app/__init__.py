# -*- codeing = utf-8 -*-
# @Time : 2021/2/10 13:59
# @Author :王小刚
# @File :__init__.py.py
# @Software：PyCharm
from flask import Flask

app = Flask(__name__)
print('等会那个包用我',__name__)

from app import routes
