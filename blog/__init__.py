from flask import Flask, render_template
from .config.variables import SECRET_KEY

def create_app():
  app = Flask(__name__)

  # CONFIGS
  app.config["SECRET_KEY"] = SECRET_KEY

  # BLUEPRINT
  from .views.admin_auth import admin
  app.register_blueprint(admin, url_prefix="/owner")

  from .views.category import category
  app.register_blueprint(category, url_prefix="/owner")


  # ERROR 404
  @app.errorhandler(404)
  def page_not_found(error):
    print("404 ERROR:", str(error))
    return render_template("error-404.html")
  

  # ERROR 500
  # @app.errorhandler(Exception)
  # def server_error(error):
  #   print("500 ERROR:", str(error))
  #   return render_template("error-500.html")
  

  return app