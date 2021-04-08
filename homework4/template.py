# imports
from flask import Flask, render_template
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

@app.route('/books')
def collages():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM books")
    html = ''    
    if response > 0:
        books = cursor.fetchall()
        return render_template('books.html', list=books)

# start server
if __name__ == '__main__':
    app.run(debug=True, port=3000)