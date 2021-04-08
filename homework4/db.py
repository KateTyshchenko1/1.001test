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


@app.route('/authors')

def AUTHORS():
    cursor = mysql.get_db().cursor()
    response = cursor.execute("SELECT * FROM AUTHORS")
    html = ''   
    if response > 0:
        AUTHORS = cursor.fetchall()
        return render_template('books.html', list=AUTHORS)

if __name__ == '__main__':
    app.run(debug=True)
