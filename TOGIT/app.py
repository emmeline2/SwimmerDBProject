from flask import Flask, render_template, redirect, url_for, request, session
import configparser
import mysql.connector
from mysql.connector import errorcode

#config file 
config = configparser.ConfigParser()
config.read('config.ini')

#app server
app = Flask(__name__)
app.secret_key = 'correct horse battery staple'

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

    if found_user == username : 
        return redirect(url_for('success'))

    #store username in session cookie
    session['name'] = username 

    sql = "select id from person where name={username}"
    swimmer_Id = sql_query(sql)
    if sql_query("select has_role from person where name = {username}") == "SWIMMER":
        session['swimmerID'] = swimmer_Id
        return redirect(url_for('success_swimmer'))
    else:
        session['coachID'] = swimmer_Id
        return redirect(url_for('success_coach'))


    #should else return failure 
    return redirect(url_for('success'))


#success swimmer
@app.route('/success_swimmer')
def success_swimmer(): 
    sql = "select id from person where name={username}"
    swimmerID = sql_query(sql)
    sql = "select stroke, distance, time, entry_id from entry where name={swimmerID}"
    entries = sql_query(sql)
    return render_template('login_success_swimmer.html')
    

#success coach
@app.route('/success_coach')
def success_coach(): 
    #return 'login html hello'
    sql = "select swimmer_id, stroke, distance, time from entry"
    entries = sql_query(sql)
    return render_template('login_success_coach.html')
    

#Add for Swimmer
@app.route('/addPageSwimmer', methods=['GET','POST'])
def addPageSwimmer(): 
    addID = request.form.get('swimmerID','') 
    stroke = request.form.get('stroke','')
    distance = request.form.get('distance','')  
    time = request.form.get('time','')
    sql = "insert into entry values({addID}, {stroke}, {distance}, {time})"
    added_value = sql_query(sql)
    return render_template('login_success_swimmer.html')

#Add for Coach
@app.route('/addPageCoach', methods=['GET','POST'])
def addPageCoach(): 
    addID = request.form.get('swimmerID','') 
    stroke = request.form.get('stroke','')
    distance = request.form.get('distance','')  
    time = request.form.get('time','')
    sql = "insert into entry values({addID}, {stroke}, {distance}, {time})"
    added_value = sql_query(sql)
    return render_template('login_success_coach.html')

@app.route('/deleteEntry', methods=['GET','POST'])
def deleteEntry(): 
    idToRemove = request.form.get('entryID',''); 
    sql = "delete from entry where {idToRemove} = entry_id"
    deleted = sql_query(sql)
    sql = "delete from entry where {idToRemove} = entry_id"
    newTable = sql_query(sql)
    return render_template('login_success_coach.html')

@app.route('/logout')
def logout(): 
    flash('You are now logged out. Redirecting to login page')
    session['name'] = ' ' 
    return redirect(url_for('login'))

if __name__ == '___main___': 
    app.secret_key = os.urandom(12)
    app.run(**config['app'])



