from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/DTM'
db = SQLAlchemy(app)

@app.route("/")
def inicio():
    return render_template("public/primeiratela.html")

@app.route("/segunda")
def segunda():
    return render_template("public/segundatela.html")

@app.route("/final")
def final():
    return render_template("public/final.html")

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)