#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Time    : 2022/2/11 4:50 PM
# @Author  : yuanhaidong
# @File    : config.py

JSON_AS_ASCII = False
# 数据库配置
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zl_flask'
USERNAME = 'root'
PASSWORD = 'qq123433.'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "12321312_asdajldjlkajlk"

# 邮箱配置
MAIL_SERVER = 'smtp.163.com'  # 使用的邮箱服务器
MAIL_PORT = 465  # 端口   支持SSL一般为465，默认为25
MAIL_USE_SSL = True  # 是否支持SSL
MAIL_USE_TLS = False  # 是否支持TLS
MAIL_DEBUG = True
MAIL_USERNAME = "17601615230@163.com"  # 用户名
MAIL_PASSWORD = "Yhd41782"  # 163邮箱客户端授权码，不是登录密码
MAIL_DEFAULT_SENDER = "17601615230@163.com"  # 默认发件人

