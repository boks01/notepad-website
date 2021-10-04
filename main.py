from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import datetime as dt

app = Flask(__name__)
app.config["SECRET_KEY"] = "nasgorenakjugaya"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data_notes.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True)
    img_url = db.Column(db.String(250), unique=True)
    body = db.Column(db.String(250), unique=True)
    author = db.Column(db.String(250), unique=True)
    date = db.Column(db.String(250), unique=True)

class DataForm(FlaskForm):
    title = StringField("Title of the blog", validators=[DataRequired()])
    author = StringField("Author name", validators=[DataRequired()])
    img_url = StringField("Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Content", validators=[DataRequired()])

db.create_all()

@app.route("/")
def home():
    notes = db.session.query(Data).all()
    return render_template("index.html", notes=notes)


if __name__ == "__main__":
    app.run(debug=True)

