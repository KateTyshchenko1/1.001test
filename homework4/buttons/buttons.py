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

@app.route('/')
def index():
    return redirect('/read')

@app.route('/createForm')
def create():
    return render_template('/create.html')

@app.route('/create', methods=['POST'])
def add():
    # Fetch form data
    author = request.form
    name = author['Author_name']
    id = author['author_id']
    email = author['author_email']
    cur = mysql.get_db().cursor()
    cur.execute("INSERT INTO authors(Author_name, Author_id, author_email) VALUES(%s, %s, %s)",(name, id, email))
    mysql.get_db().commit()
    return redirect('/read')

@app.route('/delete')
def delete():
    id = request.args.get('author_id')
    cur = mysql.get_db().cursor()
    cur.execute("DELETE FROM authors WHERE AUTHOR_ID=%s",id)
    mysql.get_db().commit()
    return redirect('/read')

@app.route('/authors')
def author():
    author = {}
    author['author_id'] = request.args.get('author_id')
    author['author_name'] = request.args.get('author_name')    
    return render_template('college.html', author=author)

@app.route('/update', methods=['POST'])
def update():
    author = request.form
    id = author['author_id']
    name = author['Author_name']
    cur = mysql.get_db().cursor()
    cur.execute("UPDATE authors SET Author_name=%s WHERE Author_id=%s",(name, id))
    mysql.get_db().commit()
    return redirect('/read')

@app.route('/read')
def read():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM authors")
    html = ''    
    if response > 0:
        authors = cursor.fetchall()
        return render_template('read.html', list=authors)

# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)