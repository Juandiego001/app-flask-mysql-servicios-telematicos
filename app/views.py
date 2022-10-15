# app/views.py
from app import app, mysql
from flask import request, render_template, redirect

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

# Route to get articles
@app.route('/articles', methods=['GET', 'POST'])
def articlesGet():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM the_article")
    the_articles = cur.fetchall()

    return render_template("articles.html", the_articles=the_articles)

# Route to add articles
@app.route('/add-articles', methods=['GET', 'POST'])
def articlesPost():
    form = request.form
    
    id = form['id']
    title = form['title']
    body = form['body']
    author = form['author']
    created_at = form['createdat']

    cur = mysql.connection.cursor()
    query = "INSERT INTO THE_ARTICLE VALUES(%s, '%s', '%s', '%s', STR_TO_DATE('%s'" % (id, title, body, author, created_at)
    query += ", '%d-%m-%Y'))"
    results = cur.execute(query)
    mysql.connection.commit()

    return redirect('/articles')

# Route to update artcles
@app.route('/edit-articles/<id>', methods=['GET', 'POST'])
def articlesPut(id):

    form = request.form
    
    idNueva = form['id']
    title = form['title']
    body = form['body']
    author = form['author']
    created_at = form['createdat']

    print(id)
    print(idNueva)
    print(title)
    print(body)
    print(author)
    print(created_at)

    cur = mysql.connection.cursor()
    query = "UPDATE THE_ARTICLE SET id = %s, title = '%s', body = '%s', author = '%s', created_date = '%s' WHERE id = %s" % (idNueva, title, body, author, created_at, id)
    results = cur.execute(query)
    mysql.connection.commit()

    return redirect('/articles')

# Route to delete artcles
@app.route('/articles/<id>', methods=['GET', 'POST'])
def articlesDelete(id):
    return redirect('/articles')
