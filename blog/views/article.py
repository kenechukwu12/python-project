from flask import Blueprint, render_template, flash, redirect
from ..utils.decorators import autheticated_admin

article = Blueprint("article", __name__)

@article.get("/add")
@autheticated_admin
def article_page():
  return render_template("admin/add-article.html")
