from flask import Blueprint, render_template, flash, redirect, abort, request, current_app
from ..utils.decorators import autheticated_admin
from ..config.database import get_connection
from ..store.category import get_all_categories
from ..store.article import get_all_articles
from ..utils.helpers import sub_words

from werkzeug.utils import secure_filename
from datetime import datetime
import os

article = Blueprint("article", __name__)
db = get_connection()

@article.get("/")
@autheticated_admin
def article_view_page():
  if not db:
    return abort(500, "Error connecting to db")
  _, cursor = db
  articles = get_all_articles(cursor, True)
  return render_template("admin/view-article.html", articles=articles, sub_words=sub_words) 

@article.get("/add")
@autheticated_admin
def article_add_page():
  if not db:
    return abort(500, "Error connecting to db")
  _, cursor = db
  categories = get_all_categories(cursor)
  return render_template("admin/add-article.html", categories=categories) 


@article.post("/create")
@autheticated_admin
def create_article():
  form = request.form
  image = request.files.get("image")

  allowed_types = ["image/png", "image/jpeg", "image/jpg"]

  if not image.mimetype in allowed_types:
    flash("File (type) not allowed", "danger")
    return redirect("/owner/article/add")
  # GET UPLOADED FILENAME
  filename = str(datetime.now().timestamp()) + "-" + secure_filename(image.filename)
  image.save(os.path.join(current_app.config["BLOG_UPLOAD_PATH"], filename))

  # GET FORM FIELDS
  title = form.get("title")
  content = form.get("content")
  author = form.get("author")
  category = form.get("category")

  if not db:
    flash("Error connecting to db", "danger")
    return redirect("/owner/article/add")
  
  conn, cursor = db

  query = "INSERT INTO article(title, image, content, author, category) VALUES (%s, %s, %s, %s, %s)"
  cursor.execute(query, [title, filename, content, author, category])
  conn.commit()

  if not cursor.rowcount: 
    flash("Failed to add article!", "danger")
    return redirect("/owner/article/add")
  
  flash("Article added successfully!", "success")
  return redirect("/owner/article/")


