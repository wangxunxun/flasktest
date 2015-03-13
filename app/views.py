#coding=utf-8
'''
Created on 2015年3月13日

@author: wangxun
'''
from flask import render_template,flash,redirect,request
from app import app 
from forms import LoginForm
from werkzeug import security
@app.route('/') 
@app.route('/index') 

def index():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template("index.html",
#        title = 'Home',
        user = user,
        posts = posts)
    
@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    print form.openid.label
    
    if request.method =='POST':
        flash('Login requested for OpenID='+str(form.openid.data)+',remember_me='+str(form.remember_me.data))
        print form.openid.data
        return redirect('/index')
    return render_template('login.html',
        title = 'Sign In',
        form = form,
        providers = app.config['OPENID_PROVIDERS']
        )
    
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')
