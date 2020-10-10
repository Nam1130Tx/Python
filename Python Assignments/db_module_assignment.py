# Python:     3.8.5
# Author:     Nicholas Mireles
# Assignemnt: DB Module

import sqlite3



filelist = ['information.docx', 'Hello.txt', 'myImage.png', \
            'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg']


         
connect = sqlite3.connect('db.assignment')

with connect:
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS txtFiles( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    Tfiles TEXT)")
    connect.commit()
    for txt in filelist:
        if txt.endswith(".txt"):
            cursor.execute("INSERT INTO txtFiles(Tfiles) VALUES (?)", \
                           (txt,))
    connect.commit
    cursor.execute("SELECT * FROM txtFiles")
    print(cursor.fetchall())
connect.close
