# -*- codeing = utf-8 -*-
# @Time : 2021/2/16 19:38
# @Author :王小刚
# @File :handlers.py
# @Software：PyCharm
from app import db
from app.errors import bp
from flask import render_template


@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


@bp.app_errorhandler(505)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
