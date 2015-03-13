#coding=utf-8
'''
Created on 2015年3月13日

@author: wangxun
'''
from flask import Flask 
app = Flask(__name__) 
app.config.from_object('config')
from app import views