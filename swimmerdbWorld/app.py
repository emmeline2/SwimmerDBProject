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

@app.route('/success/<name>')
def success(name): 
    return 'welcome %s' % name

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
