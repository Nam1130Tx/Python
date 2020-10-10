# Python:     3.8.5
# Author:     Nicholas Mireles
# Assignemnt: DB Module

import sqlite3


def start():
    filelist = ['information.docx', 'Hello.txt', 'myImage.png', \
                'myMovie.mpg', 'World.txt', 'data.pdf', 'myPhoto.jpg']

    text_files = []

    for match in filelist:
        if "txt" in match:
            text_files.append(match)
    return(text_files)

         
connect = sqlite3.connect('db.assignment')

with connect:
    cursor = connect.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS txtFiles( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    Tfiles TEXT)")
    connect.commit()
    cursor.execute("INSERT  INTO txtFiles(Tfiles) \
                    VALUES ('Hello.txt'), ('World.txt')")
    connect.commit
    cursor.execute("SELECT * FROM txtFiles")
    print(cursor.fetchall())
connect.close
