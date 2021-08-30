import sqlite3
from database import DB_NAME
class User():
    def __init__(self,name:str,id:int,dna:float=0):
        self.__name=name
        self.__id=id
        self.__dna_perc=int(dna*100)
        self.__notes=self.__findNotes()

    def __findNotes(self):
        db=sqlite3.connect(DB_NAME)
        cursor=db.cursor()
        query="SELECT data,date,Id FROM Notebooks\
               WHERE userId="+str(self.__id)
        result=cursor.execute(query)
        notes=[]
        for res in result:
            notes.append(res)
        db.close()
        return notes
    def getName(self):
        return self.__name
    def getId(self):
        return self.__id
    def getNotes(self):
        return self.__notes
    def getDna(self):
        return self.__dna_perc

    def addNote(self,data:str,date:str):
        db = sqlite3.connect(DB_NAME)
        cursor = db.cursor()
        query = "SELECT MAX(Id) FROM Notebooks"
        result = cursor.execute(query)
        id=0
        for res in result:
            id=res[0]
        db.close()
        self.__notes.append((data,date,id))

    def deleteNote(self,note_id):
        for index,note in enumerate(self.__notes):
            if note[2]==note_id:
                self.__notes.pop(index)
                break
