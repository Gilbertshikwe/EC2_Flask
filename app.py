from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

# Configure MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'flaskuser'
app.config['MYSQL_PASSWORD'] = 'flaskpassword'
app.config['MYSQL_DB'] = 'flask_app_db'

# Initialize MySQL
mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM users")
    users = cur.fetchall()
    return render_template('index.html', users=users)

@app.route('/add', methods=['POST'])
def add_user():
    name = request.form['name']
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users(name) VALUES (%s)", [name])
    mysql.connection.commit()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
