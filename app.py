#route for login page logic 

@app.route('/login',method=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST'
        if request.form['username'] != 'admin' or request.form['password'] != 'admin': 
            error = 'Invaid credentials. Try again please.'
        else: 
            return redirect(url_for('home'))
    return render_template('home.html', error=error)


