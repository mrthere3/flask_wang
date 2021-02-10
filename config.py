# -*- codeing = utf-8 -*-
# @Time : 2021/2/10 20:59
# @Author :王小刚
# @File :config.py
# @Software：PyCharm
import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'