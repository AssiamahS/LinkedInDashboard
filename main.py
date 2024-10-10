from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)

def create_connection():
    conn = sqlite3.connect('applications.db')
    return conn

def create_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS applications (id INTEGER PRIMARY KEY, user TEXT, count INTEGER)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = create_connection()
    c = conn.cursor()
    c.execute('SELECT user, count FROM applications')
    data = c.fetchall()
    conn.close()
    return render_template('index.html', data=data)

@app.route('/update', methods=['POST'])
    conn = create_connection()
    c = conn.cursor()
    user = request.form['user']
    count = request.form['count']
    c.execute('INSERT INTO applications (user, count) VALUES (?, ?)', (user, count))
    conn.commit()
    conn.close()
    return jsonify(success=True)

if __name__ == '__main__':
    create_table()
    app.run(debug=True)
