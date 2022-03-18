#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Time    : 2022/3/18 2:28 PM
# @Author  : yuanhaidong
# @File    : demand_paging.py
from flask import request


def paging(model=None):
    page = request.args.get("page", 1, type=int)
    per_page = int(request.args.get('per_page', 10))
    paginate = model.query.order_by(model.id.desc()).filter_by(isDelete=0).paginate(page, per_page,
                                                                                    error_out=False)
    return paginate
