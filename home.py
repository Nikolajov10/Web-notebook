from flask import Flask,Blueprint,render_template,flash
home=Blueprint("home",__name__)
@home.route("/home")
@home.route("/")
def homePage():
    from auth import user
    return render_template("home.html",user=user)
