# -*- codeing = utf-8 -*-
# @Time : 2021/2/10 14:05
# @Author :王小刚
# @File :routes.py
# @Software：PyCharm
from app import app
from app.forms import LoginForm
from flask import render_template, flash, redirect


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [  # 创建一个列表：帖子。里面元素是两个字典，每个字典里元素还是字典，分别作者、帖子内容。
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()  # 表单实例化对象
    if form.validate_on_submit():  # validate get请求通过是ture post是flase
        flash('Login requested for user {},remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', title='Sign In', form=form)
