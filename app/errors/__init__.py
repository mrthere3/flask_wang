#-*- codeing = utf-8 -*-
#@Time : 2021/2/16 19:37
#@Author :王小刚
#@File :__init__.py
#@Software：PyCharm
from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers
