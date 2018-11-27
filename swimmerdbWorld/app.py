#!/usr/bin/python3

#route for login page logic 
from flask import Flask, render_template, redirect, url_for, request
import configparser

#config file 
config = configparser.ConfigParser()
config.read('config.ini')

#app server
app = Flask(__name__)

#@app.route('/')
def basic_response(): 
    return "It works!"

@app.route('/')
def template_response(): 
    return render_template('home.html')

#@app.route('/', method=['GET', 'POST'])
def login():
    print(login.form)
    error = None
    if request.method == 'POST': 
        if request.form['username'] != 'admin' or request.form['password'] != 'admin': 
            error = 'Invaid credentials. Try again please.'
        else: 
            return redirect(url_for('/'))
    return render_template('home.html', error=error)

if __name__ == '___main___': 
    app.run(**config['app'])
