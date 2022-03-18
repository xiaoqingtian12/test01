#!/usr/bin/ python
# -*- coding: utf-8 -*-
# @Software: PyCharm
# @Time    : 2022/3/16 9:49 AM
# @Author  : yuanhaidong
# @File    : ding_send.py
from dingtalkchatbot.chatbot import DingtalkChatbot


# https://oapi.dingtalk.com/robot/send?access_token=4e55d43124d21c4ebf213b639a84c0c8d564b0b13caf0461b8f4dc920e01f21c
def send_message(message):
    webhook = 'https://oapi.dingtalk.com/robot/' \
              'send?access_token=4e55d43124d21c4ebf213b639a84c0c8d564b0b13caf0461b8f4dc920e01f21c'
    dingding = DingtalkChatbot(webhook)
    dingding.send_text(msg=message, is_at_all=True)



