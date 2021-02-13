# -*- codeing = utf-8 -*-
# @Time : 2021/2/10 20:59
# @Author :王小刚
# @File :config.py
# @Software：PyCharm
import os

basedir = os.path.abspath(os.path.dirname(__file__))  # 获取当前.py文件的绝对路径


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
# 王小刚的修改