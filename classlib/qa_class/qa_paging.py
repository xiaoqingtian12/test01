#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Time    : 2022/3/18 2:05 PM
# @Author  : yuanhaidong
# @File    : qa_paging.py
from flask import request
from exts import db


def paging(model=None):
    page = request.args.get("page", 1, type=int)
    per_page = int(request.args.get('per_page', 10))
    paginate = model.query.filter_by(isDelete=0).order_by(db.text("-create_time")).paginate(page, per_page,
                                                                                            error_out=False)
    return paginate
