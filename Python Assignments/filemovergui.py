import tkinter as tk
from tkinter import ttk
import os
import time
import shutil
import datetime

#method used to sort files by time and choose which files to move
def shuttle():
    now = datetime.datetime.now() #getting the current time
    ago = now-datetime.timedelta(hours=24)#using timedelta to identify files modified less then 24 hours
    strftime = "%H:%M %m/%d/%Y" #this is more for printing a line in the shell so i know action was completed
    src = 'C:/Users/mirel/OneDrive/Desktop/TempDesktop/Hold' #variable setting my source file
    dest = 'C:/Users/mirel/OneDrive/Desktop/TempDesktop/Transfer' #variable setting my destination file

    for root,dirs,files in os.walk(src): #for loop to look thru the 1st folder to find the specified files
        for name in files:
            path = os.path.join(root,name)
            st = os.stat(path)
            mtime = datetime.datetime.fromtimestamp(st.st_mtime)
            if mtime > ago: #if loop to determine what files should be moved, and to print to shell and use shutil to actually move the files.
                print("True: ", name, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
                shutil.copy(path, dest)


hold = 'C:/Users/mirel/OneDrive/Desktop/TempDesktop' #setting the variable for the comboboxes
holdlist = [hname for hname in os.listdir(hold)]

trans = 'C:/Users/mirel/OneDrive/Desktop/TempDesktop'
translist = [tname for tname in os.listdir(trans)]

master = tk.Tk() #Building the Window
master.geometry('175x200')
master.title('Select a file')

tk.Label(master, text='Send from:').grid(column=0,row=0,padx=5)
tk.Label(master, text='Send To:').grid(column=0,row=2,padx=5)


tk.Button(master, text='Transfer',command=shuttle).grid(column=0,row=4,pady=5) #Sets the button to execute shuttle()

opt1 = ttk.Combobox(master, values=holdlist).grid(column=0,row=1,padx=5)
opt2 = ttk.Combobox(master, values=translist).grid(column=0,row=3,padx=5)


master.mainloop()
