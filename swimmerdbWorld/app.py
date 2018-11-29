#!/usr/bin/python3

#route for login page logic 
from flask import Flask, render_template, redirect, url_for, request, session
import configparser
import mysql.connector

#config file 
config = configparser.ConfigParser()
config.read('config.ini')

#app server
app = Flask(__name__)


#SQL querry set up 
@app.route('/', methods=['GET','POST'])
def start():
    return render_template('login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login(): 
    username = request.form.get('name',''); 
    password = request.form.get('password', '')

    #store username in session cookie
    #session['name'] = username 

    return redirect(url_for('success'))

@app.route('/success')
def success(): 
    #return 'login html hello'
    return render_template('login_success_swimmer.html')
    #return "yay successsss!"

if __name__ == '___main___': 
    app.run(**config['app'])
