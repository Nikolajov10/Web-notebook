import sqlite3
from datetime import datetime

DB_NAME="users.db"
def createDatabase():
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    query_create = "CREATE TABLE IF NOT EXISTS Users(\
                Id INTEGER PRIMARY KEY AUTOINCREMENT,\
                name VARCHAR(40) UNIQUE,\
                email VARCHAR(100) UNIQUE,\
                password VARCHAR(30),\
                dna TEXT)"

    cursor.execute(query_create)
    db.commit()
    db.close()
    createNotebookTable()
def createNotebookTable():
    db=sqlite3.connect(DB_NAME)
    cursor=db.cursor()
    query_create="CREATE TABLE IF NOT EXISTS Notebooks(\
    Id INTEGER PRIMARY KEY AUTOINCREMENT,\
    data TEXT,\
    date TEXT,\
    userId INTEGER REFERENCES Users(Id))"
    cursor.execute(query_create)
    db.commit()
    db.close()
def insertNote(data,date,userID):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    query_create = "INSERT INTO Notebooks(data,date,userId)\
                    VALUES (?,?,?);"
    values=(data,date,userID)
    cursor.execute(query_create,values)
    db.commit()
    db.close()
def deleteNote(noteId):
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    query_create = "DELETE FROM Notebooks\
    WHERE Id="+str(noteId)
    cursor.execute(query_create)
    db.commit()
    db.close()
