# -*- codeing = utf-8 -*-
# @Time : 2021/2/10 14:05
# @Author :王小刚
# @File :routes.py
# @Software：PyCharm
from app import app
from flask import render_template


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

