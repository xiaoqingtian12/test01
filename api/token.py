#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Time    : 2022/3/11 11:29 AM
# @Author  : yuanhaidong
# @File    : token.py
import requests
from api import data_storage
from flask import request


def login_token(account=None):
    url = 'https://tapi.voglassdc.com/oauth/v1/Login/token'
    body = {
        "Account": account,
        "Password": "xxzx2020@123"
    }

    header = {
        "Content-Type": "application/json",
        "s": "1001"
    }

    res = requests.request("post", json=body, headers=header, url=url).json()
    data_storage.data_token = res['data']['token']
