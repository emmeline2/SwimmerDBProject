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

def sql_query(sql): 
    #db = mysql.connector.connect(**config['mysql.connector'])
    try: 
    db = mysql.connector.connect(user= 'root', password='db2018', host = '127.0.0.1', database='webdatabase')
    
    cursor = db.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    db.close()
    return result

def sql_execute(sql): 
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()

#SQL querry set up 
@app.route('/', methods=['GET','POST'])
def start():
    return render_template('login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login(): 
    username = request.form.get('name',''); 
    password = request.form.get('password', '')

    sql = "select * from person where name={username}"
    found_user = sql_query(sql)
    print(found_user)
    print(username)

    #store username in session cookie
    #session['name'] = username 

    return redirect(url_for('success'))

@app.route('/success')
def success(): 
    #return 'login html hello'
    return render_template('login_success_swimmer.html')
    #return "yay successsss!"

@app.route('/logout')
def logout(): 
    flash('You are now logged out. Redirecting to login page')
    return redirect(url_for('login'))

if __name__ == '___main___': 
    app.run(**config['app'])
