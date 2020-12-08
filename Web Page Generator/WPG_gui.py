from tkinter import *
from tkinter import scrolledtext
import webbrowser    

#Used to take text from the entry box and input it into "message" as a variable
#Then writes the file and uses webrowser to display in default browser.
def submitTxt():
    f = open('index.html','w')
    txt = src.get()
    message = "<html><head></head><body><h1>%s</h1></body></html>" % txt
    f.write(message)
    f.close()
    webbrowser.open_new_tab('index.html')

#Clears the entry box of any text.
def clearTxt():
    txt.delete(0,'end')

#Creates and maps out the window using the grid format.
window = Tk()
src = StringVar()   

#General window Creation
window.geometry('275x150')
window.title("Web Page Generator GUI")

#Label Creation
lbl = Label(window, text="Enter Your Web Page Text:")
lbl.grid(column=0,row=0,padx=5)

#Entry box creation
txt = Entry(window,width=20,textvariable=src)
txt.grid(column=0,row=1,padx=5)

#Button creations, uses command to set them to the above functions.
btn = Button(window,text="Clear",command=clearTxt)
btn.grid(column=0,row=12,pady=5,padx=13,sticky=W)
btn = Button(window,text="Submit",command=submitTxt)
btn.grid(column=0,row=12,pady=5,padx=17,sticky=E)

window.mainloop() #Keeps the window running till closed.
