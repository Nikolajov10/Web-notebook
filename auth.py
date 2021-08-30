from flask import Flask,Blueprint,render_template,request,redirect,url_for,flash,jsonify
import sqlite3
from User import User
import json
from datetime import date
from home import home
from helpFun import *

auth=Blueprint("auth",__name__)
user:User=None

@auth.route("/login-wrapper")
def wrraper_login():
    global user
    if user:
        return redirect(url_for("home.homePage",user=user))
    else:
        return redirect(url_for("auth.login", user=user))

error_flag=False

@auth.route("/login",methods=["POST","GET"])
def login():
    global user,error_flag
    if user==None and error_flag==True:
        error_flag=False
        flash("Wrong user name or password!","error")
        return render_template("login.html", user=user)
    if request.method == "POST":
        data = json.loads(request.data)
        dna1 = data['DNA']
        name=data['name']
        password=data["password"]
        db=sqlite3.connect("users.db")
        cursor=db.cursor()
        query="SELECT Id,dna FROM Users WHERE name=? AND password=?"
        values=(name,password)
        result=cursor.execute(query,values)
        for r in result:
            dna2=arrStrToArr(r[1])
            dna_percentage=compareDNAs(dna1,dna2)
            user = User(name,r[0],dna_percentage)
            error_flag=False
            return redirect(url_for("auth.notebook",user=user))
        error_flag=True
    return render_template("login.html",user=user)

@auth.route("/reg-wrapper")
def wrraper_reg():
    global user
    if user==None:
        return redirect(url_for("auth.register",user=user))
    return redirect(url_for("home.homePage",user=user))

@auth.route("/register",methods=["POST","GET"])
def register():
    global user
    if request.method == "POST":
        data = json.loads(request.data)
        name=data['name']
        email = data["email"]
        password1= data["password1"]
        password2 = data["password2"]
        dna=data['DNA']
        print(dna,email,password1)
        if password1!=password2:
            flash("Passwords are not correct!","error")
        else:
            db=sqlite3.connect('users.db')
            query_emails="SELECT email,name FROM Users"
            cursor = db.cursor()
            result=cursor.execute(query_emails)
            for res in result:
                if res[0]==email:
                    flash("Email address already taken!","error")
                    return render_template("register.html",user=user)
                elif res[1]==name:
                    flash("User name already taken!", "error")
                    return render_template("register.html",user=user)
            query="INSERT INTO Users(name,email,password,dna) VALUES (?,?,?,?)"
            values=(name,email,password1,str(dna))
            cursor.execute(query,values)
            db.commit()
            query = "SELECT MAX(Id) FROM Users"
            result = cursor.execute(query)
            id=0
            for r in result:
                id=r[0]
            db.close()
            user = User(name,id)
            return redirect(url_for("auth.notebook",user=user))
    return render_template("register.html",user=user)

@auth.route("/logout")
def logout():
    global user
    user=None
    return render_template("logout.html",user=user)


@auth.route("/notebook",methods=["POST","GET"])
def notebook():
    global user
    if user == None:
        return redirect(url_for("auth.login",user=user))
    if request.method=="POST":
        from database import insertNote
        note=request.form.get("note")
        if len(note)<=1:
            return render_template("notebook.html", user=user)
        today=reverseDateString(str(date.today()))
        insertNote(note,today,user.getId())
        user.addNote(note, today)
    return render_template("notebook.html",user=user)

@auth.route('/delete-note', methods=['POST'])
def delete_note():
    global user
    if user!=None:
        note = json.loads(request.data)
        noteId = note['noteId']
        from database import deleteNote
        deleteNote(noteId)
        user.deleteNote(noteId)
    return jsonify({})