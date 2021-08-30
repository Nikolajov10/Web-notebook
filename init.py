from flask import Flask
from home import home
from auth import auth

def createApp():
    app = Flask(__name__)
    app.config["SECRET_KEY"]= "hello"
    app.register_blueprint(home, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    return app
