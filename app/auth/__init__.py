#-*- codeing = utf-8 -*- 
#@Time : 2021/2/16 19:49
#@Author :王小刚
#@File :__init__.py.py
#@Software：PyCharm
from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes