# -*- codeing = utf-8 -*-
# @Time : 2021/2/10 21:14
# @Author :王小刚
# @File :forms.py
# @Software：PyCharm
from flask_wtf import FlaskForm  # 从flask_wtf包中导入FlaskForm类
from wtforms import StringField, PasswordField, BooleanField, SubmitField  # 导入这些类
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])#d函数保证建议的对话框不能为空
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')
