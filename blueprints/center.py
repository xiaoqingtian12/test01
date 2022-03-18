#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Time    : 2022/3/3 11:00 AM
# @Author  : yuanhaidong
# @File    : center.py
from flask import Blueprint, render_template, url_for, request, flash, redirect
from blueprints.forms import AddPersonalCenterForm
from models import UserModel
from exts import db
from decorators import login_required
from datetime import datetime

bp = Blueprint("center", __name__, url_prefix="/personal")


@bp.route("/", methods=["GET", "POST"])
@login_required
def center_list():
    return render_template("center/Personal_Center.html")


@bp.route("/add", methods=["GET", "POST"])
@login_required
def center_add():
    if request.method == 'GET':
        return render_template("center/Personal_Center.html")
    else:
        email = request.form.get("email")
        form = AddPersonalCenterForm(request.form)
        if form.validate():
            user = UserModel.query.filter_by(email=email).first()
            if user:
                user.age = form.age.data
                user.sex = form.sex.data
                user.mobile = form.mobile.data
                user.address = form.address.data
                user.update_time = datetime.now()
                db.session.commit()
                return redirect(url_for("center.center_list"))
            else:
                flash("没有此数据")
                return render_template("center/Personal_Center.html")
        else:
            flash("校验未通过")
            return render_template("center/Personal_Center.html")
