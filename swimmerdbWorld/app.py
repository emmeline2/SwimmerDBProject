#!/usr/bin/python3

#route for login page logic 
from flask import Flask, render_template, redirect, url_for, request
import configparser
import mysql.connector

#config file 
config = configparser.ConfigParser()
config.read('config.ini')

#app server
app = Flask(__name__)


#SQL querry set up 
'''
def sql_query(sql): 
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor() 
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    return result

def sql_execute(sql): 
    db = mysql.connector.connect(**config['mysql.connector'])
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    cursor.close()
    db.close()
'''


@app.route('/')
def template_response(): 
    return render_template('home.html')

@app.route('/success/<name>')
def success(name): 
    #return 'login html hello'
    return render_template('login.html')

@app.route('/login', methods = ['POST', 'GET'])
def login(): 
    if request.method == 'POST': 
        user = request.form['nm']
        return redirect(url_for('success', name = user))
    else: 
        user = request.args.get('nm')
        return redirect(url_for('success', name = user))


if __name__ == '___main___': 
    app.run(**config['app'])
