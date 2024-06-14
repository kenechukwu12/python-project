# Flask Blog Project

## Introduction
This project is a simple blog web page built using the Flask web framework in Python. It includes functionalities to list blog posts, view individual posts, and create new posts.

## Project Structure
my_blog/
│
├── app.py
├── templates/
│ ├── base.html
│ ├── index.html
│ ├── post.html
│ ├── new_post.html
├── static/
│ ├── css/
│ ├── js/
│ ├── images/
├── models.py
├── forms.py
└── config.py

## Setup Instructions

### Step 1: Install Dependencies
Ensure you have Python and pip installed. Install Flask and other dependencies:
```bash
pip install Flask Flask-WTF Flask-SQLAlchemy
Step 2: Configuration

Create a config.py file to manage configuration settings:

python

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

Step 3: Database Models

Define the database model for blog posts in models.py:

python

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

Step 4: Forms

Define forms for creating new posts in forms.py:

python

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class BlogPostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

Step 5: Flask Application

Initialize your Flask application in app.py:

python

from flask import Flask, render_template, request, redirect, url_for
from models import db, BlogPost
from forms import BlogPostForm

app = Flask(__name__)
app.config.from_object('config.Config')

db.init_app(app)

@app.route('/')
def index():
    posts = BlogPost.query.all()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return render_template('post.html', post=post)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        post = BlogPost(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('new_post.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)

Step 6: Templates

Create HTML templates in the templates/ directory:
base.html

html

<!DOCTYPE html>
<html>
<head>
    <title>My Blog</title>
    <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <div class="container">
        <header>
            <h1>My Blog</h1>
        </header>
        <nav>
            <a href="{{ url_for('index') }}">Home</a>
            <a href="{{ url_for('new_post') }}">New Post</a>
        </nav>
        <main>
            {% block content %}{% endblock %}
        </main>
    </div>
</body>
</html>

index.html

html

{% extends 'base.html' %}

{% block content %}
    <h2>Blog Posts</h2>
    <ul>
    {% for post in posts %}
        <li>
            <a href="{{ url_for('post', post_id=post.id) }}">{{ post.title }}</a>
            <p>{{ post.created_at.strftime('%Y-%m-%d') }}</p>
        </li>
    {% endfor %}
    </ul>
{% endblock %}

post.html

html

{% extends 'base.html' %}

{% block content %}
    <h2>{{ post.title }}</h2>
    <p>{{ post.content }}</p>
    <p><small>Posted on {{ post.created_at.strftime('%Y-%m-%d') }}</small></p>
{% endblock %}

new_post.html

html

{% extends 'base.html' %}

{% block content %}
    <h2>New Post</h2>
    <form method="post">
        {{ form.hidden_tag() }}
        <p>
            {{ form.title.label }}<br>
            {{ form.title(size=32) }}
        </p>
        <p>
            {{ form.content.label }}<br>
            {{ form.content(rows=10) }}
        </p>
        <p>{{ form.submit() }}</p>
    </form>
{% endblock %}

Step 7: Running the Application

Initialize the database and run the Flask application:

bash

export FLASK_APP=app.py
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
flask run

Features

    Home Page: Lists all blog posts.
    Post Page: Displays the content of a single post.
    New Post: Form to create a new blog post.

Future Enhancements

    Add user authentication for post creation and management.
    Implement comments on posts.
    Enhance the design with CSS and JavaScript.

Conclusion

This project provides a basic setup for a blog web application using Flask. It can be further extended and customized as per your requirements.

arduino


This README provides a clear and concise guide for setting up and running the Flask blog project. It covers project structure, setup instructions, and features.

