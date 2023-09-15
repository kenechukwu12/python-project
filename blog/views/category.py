from flask import Blueprint, render_template
from ..utils.decorators import autheticated_admin


category = Blueprint("category", __name__)

@category.get("/category")
@autheticated_admin
def category_page():
  return render_template("admin/category.html")