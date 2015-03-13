#coding=utf-8
'''
Created on 2015年3月13日

@author: wangxun
'''

from wtforms import Form, TextField, BooleanField
 
class LoginForm(Form):
    openid = TextField('openid')
    remember_me = BooleanField('remember_me', default = False)
    