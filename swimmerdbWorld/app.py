from flask import Flask, render_template, redirect, url_for, request, session
import configparser
import mysql.connector
from mysql.connector import errorcode

#config file 
config = configparser.ConfigParser()
config.read('config.ini')

#app server
app = Flask(__name__)

def sql_query(sql): 
    
    try: 
        db = mysql.connector.connect(**config['mysql.connector'])
        #db = mysql.connector.connect(user='new_user', password='db2018', host = '127.0.0.1', database='webdatabase', auth_plugin='mysql_native_password')
    except mysql.connector.Error as err: 
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR: 
            print("somethig is wrong with your credentials ")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return "error setting up database connection"
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

    sql = "select password from person where name={username}"
    found_user = sql_query(sql)
    print(found_user)
    print(username)

    if found_user == username : 
        print("yayyyy you are validated")
        return redirect(url_for('success'))

    #store username in session cookie
    session['name'] = username 

    sql = "select id from person where name={username}"
    swimmer_Id = sql_query(sql)
    session['swimmerID'] = swimmer_Id

    #should else return failure 
    return redirect(url_for('success'))

@app.route('/success')
def success(): 
    #return 'login html hello'
    return render_template('login_success_swimmer.html')
    #return "yay successsss!"

#Add for Swimmer
@app.route('/addPage')
def addPage(): 
    sql = "insert into entry values(id, stroke, time, distance)"
    added_value = sql_query(sql)
    return render_template('login_success_swimmer.html')

#Add for Coach
@app.route('/addPageCoach')
def addPage(): 
    sql = "insert into entry values(id, stroke, time, distance)"
    added_value = sql_query(sql)
    return render_template('login_success_coach.html')


@app.route('/logout')
def logout(): 
    flash('You are now logged out. Redirecting to login page')
    return redirect(url_for('login'))

if __name__ == '___main___': 
    app.run(**config['app'])



