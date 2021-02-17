# -*- codeing = utf-8 -*-
# @Time : 2021/2/16 19:59
# @Author :王小刚
# @File :microblog.py
# @Software：PyCharm
from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}


if __name__ == '__main__':
    app.run()
