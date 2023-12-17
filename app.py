from flask import Flask, render_template, request, flash, session, redirect
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/register', methods=['GET', 'POST'])
def creating():
    if request.method == 'POST':
        first = request.form['first_name']
        last = request.form['last_name']
        username = request.form['username']
        password = request.form['password']
        with sql.connect('blogging.db') as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO user (first_name,\
                        last_name, username, password) VALUES (?,?,?,?)",
                        (first, last, username, password))
            conn.commit()
        return redirect('/login')
    return render_template('creating.html')

@app.route('/login', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        username = request.form['username']
        with sql.connect('blogging.db') as conn:
            cur = conn.cursor()
            user_pw = cur.execute("SELECT password \
FROM user WHERE username = ?", (username,))
            if list(user_pw) == request.form['password']:
                session['login'] = True
                session['first_name'] = user['first_name']
                session['last_name'] = user['last_name']
        return redirect('/')
    return render_template('signin.html')

@app.route('/write', methods=['GET', 'POST'])
def creating_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        with sql.connect('blogging.db') as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO blog\
(title, body) VALUES (?,?)", (title, body))
            conn.commit()
        return redirect('/')
    return render_template('creating_post.html')

@app.route('/myblog')
def myblogs():
    with sql.connect('blogging.db') as conn:
        conn.row_factory = sql.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM blog')
        rows = cur.fetchall()
        return render_template('myblog.html', rows=rows)

@app.route('/delblog')
def delete():
    return render_template('delete.html')

@app.route('/delrec', methods=['POST', 'GET'])
def delrec():
    if request.method == 'POST':
        try:
            title = request.form['title']
            with sql.connect("blogging.db") as con:
                cur = con.cursor()
                cur.execute("DELETE FROM blog WHERE title = ?",
                            (title,))
                con.commit()
        except:
            conn.rollback()

    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)




