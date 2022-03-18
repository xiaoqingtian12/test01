#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Time    : 2022/2/18 11:16 AM
# @Author  : yuanhaidong
# @File    : models.py
from exts import db
from datetime import datetime


class EmailCaptchaModel(db.Model):
    __tablename__ = "email_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=False)
    captcha = db.Column(db.String(100), nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now)


class UserModel(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=True)
    sex = db.Column(db.String(2), nullable=True)
    mobile = db.Column(db.String(20), nullable=True)
    address = db.Column(db.String(50), nullable=True)
    update_time = db.Column(db.DateTime, default=datetime.now)
    join_time = db.Column(db.DateTime, default=datetime.now)


class QuestionModel(db.Model):
    __tablename__ = "question"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    modular = db.Column(db.Text, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    request_method = db.Column(db.String(29), nullable=False)
    content = db.Column(db.Text, nullable=False)
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, default=datetime.now())
    isDelete = db.Column(db.Integer)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship("UserModel", backref="questions")


class DemandModel(db.Model):
    __tablename__ = "demand"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    demand_name = db.Column(db.Text, nullable=False)
    demand_href = db.Column(db.String(200), nullable=False)
    pm_name = db.Column(db.Text, nullable=True)
    rd_name = db.Column(db.Text, nullable=True)
    test_name = db.Column(db.Text, nullable=True)
    status = db.Column(db.Integer, default=0)
    isDelete = db.Column(db.Integer, default=0)
    test_time = db.Column(db.DateTime, nullable=True)
    online_time = db.Column(db.DateTime, nullable=True)
    create_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(db.DateTime, nullable=True)

    author_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    author = db.relationship("UserModel", backref="demands")
