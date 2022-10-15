# app/__init__.py
from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__, instance_relative_config=True)
app.config.from_object("config")

# Adding initial data
# if there is not inserted on the database
with app.app_context():
    mysql = MySQL(app)

    articles = [
        {
            'id': 1,
            'title': 'Article One',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'author': 'Mondragon',
            'create_date': '24-10-2018'
        },
    
        {
            'id': 2,
            'title': 'Article Two',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'author': 'Martinez',
            'create_date': '24-10-2018'
        },
    
        {
            'id': 3,
            'title': 'Article Three',
            'body': 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
            'author': 'Perez',
            'create_date': '24-10-2018'
        }
    ]
    
    cur = mysql.connection.cursor()
    results = cur.execute("SELECT * FROM the_article")

    if results == 0:
        for article in articles:
            query_insert = "INSERT INTO the_article VALUES(%s, '%s', '%s', '%s', STR_TO_DATE('%s'"

            id = article['id']
            title = article['title']
            body = article['body']
            author = article['author']
            create_date = article['create_date']
            

            query_insert = query_insert % (id, title, body, author, create_date)
            query_insert += ", '%d-%m-%Y'))"

            results_querys = cur.execute(query_insert)
            mysql.connection.commit()

from app import views