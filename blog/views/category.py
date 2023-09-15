from flask import Blueprint, render_template

category = Blueprint("category", __name__)

@category.get("/category")
def category_page():
  return render_template("admin/category.html")