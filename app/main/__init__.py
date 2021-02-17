#-*- codeing = utf-8 -*- 
#@Time : 2021/2/16 19:54
#@Author :王小刚
#@File :__init__.py
#@Software：PyCharm
from flask import Blueprint

bp = Blueprint('main', __name__)

from app.main import routes

