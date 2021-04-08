# imports
from flask import Flask, render_template, request, redirect
from flaskext.mysql import MySQL

# web application
app = Flask(__name__)

# connect to db
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Kiskakat1'
app.config['MYSQL_DATABASE_DB'] = 'books'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/createForm')
def create():
    return render_template('/create.html')

@app.route('/create', methods=['POST'])
def add():
    # Fetch form data
    AUTHORS = request.form
    name = AUTHORS['Author_name']
    email = AUTHORS['Author_email']
    cur = mysql.get_db().cursor()
    cur.execute("INSERT INTO colleges(Author_name, Author_email) VALUES(%s, %s)",(Author_name, Author_email))
    mysql.get_db().commit()
    return redirect('/read')

@app.route('/read')
def read():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM authors")
    html = ''    
    if response > 0:
        AUTHORS = cursor.fetchall()
        return render_template('read.html', list=authors)
        
# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)