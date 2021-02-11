# -*- codeing = utf-8 -*-
# @Time : 2021/2/10 14:14
# @Author :王小刚
# @File :microblog.py
# @Software：PyCharm
from app import app, db
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    app.run(debug=True)
