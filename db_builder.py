#Clyde "Thluffy" Sinclair
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

def peep_open():
    with open("peeps.csv") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            return "INSERT INTO discobandit VALUES (" + row["name"] +"," + \
                    row["age"] + "," + row["id"] + ");"

##NEED TO FINISH THIS FUNCTION
      

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

command = "CREATE TABLE discobandit (name TEXT, age INTEGER, id INTEGER);"
peep_open() 
#build SQL stmt, save as string
c.execute(command)    #run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


