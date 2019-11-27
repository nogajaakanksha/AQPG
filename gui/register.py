from Tkinter import *
import sqlite3
import login
import sys
import os


#==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `useraccount` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, uname TEXT, subjectname TEXT, classname TEXT, mobileno TEXT, username TEXT, password TEXT)")       
    cursor.execute("INSERT INTO `useraccount` ('uname','subjectname','classname','mobileno','username', 'password') VALUES('"+str(NAME.get())+"', '"+str(SUBJECTNAME.get())+"', '"+str(CLASSNAME.get())+"', '"+str(MOBILENO.get())+"', '"+str(USERNAME.get())+"','"+str(PASSWORD.get())+"')")
    conn.commit()
    
def RegisterUser(event=None):
    Database()

    if USERNAME.get() == "" or PASSWORD.get() == "":
        lbl_text.config(text="Please complete the required field!", fg="red")
    else:
        HomeWindow()   

    cursor.close()
    conn.close()

def HomeWindow():
    root.destroy()
    login.gui()
def gui():
    global root
    root = Tk()
    root.title("Registration Application")
    width = 700
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    #==============================VARIABLES======================================
    global NAME,SUBJECTNAME,CLASSNAME,MOBILENO,USERNAME,PASSWORD
    NAME = StringVar()
    SUBJECTNAME = StringVar()
    CLASSNAME = StringVar()
    MOBILENO = StringVar()
    USERNAME = StringVar()
    PASSWORD = StringVar()

    #==============================FRAMES=========================================
    Top = Frame(root, bd=2,  relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(root, height=200)
    Form.pack(side=TOP, pady=20)

    #==============================LABELS=========================================
    lbl_title = Label(Top, text = "Registration Application", font=('arial', 15))
    lbl_title.pack(fill=X)
    lbl_name = Label(Form, text = "Name:", font=('arial', 14), bd=15)
    lbl_name.grid(row=0, sticky="e")
    lbl_subjectname = Label(Form, text = "Subject Name:", font=('arial', 14), bd=15)
    lbl_subjectname.grid(row=1, sticky="e")
    lbl_classname = Label(Form, text = "Class Name:", font=('arial', 14), bd=15)
    lbl_classname.grid(row=2, sticky="e")
    lbl_mobileno = Label(Form, text = "Mobile No:", font=('arial', 14), bd=15)
    lbl_mobileno.grid(row=3, sticky="e")
    lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
    lbl_username.grid(row=4, sticky="e")
    lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
    lbl_password.grid(row=5, sticky="e")
    lbl_text = Label(Form)
    lbl_text.grid(row=6, columnspan=2)

    #==============================ENTRY WIDGETS==================================
    name = Entry(Form, textvariable=NAME, font=(14))
    name.grid(row=0, column=1)
    subjectname = Entry(Form, textvariable=SUBJECTNAME, font=(14))
    subjectname.grid(row=1, column=1)
    classname = Entry(Form, textvariable=CLASSNAME, font=(14))
    classname.grid(row=2, column=1)
    mobileno = Entry(Form, textvariable=MOBILENO, font=(14))
    mobileno.grid(row=3, column=1)
    username = Entry(Form, textvariable=USERNAME, font=(14))
    username.grid(row=4, column=1)
    password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
    password.grid(row=5, column=1)

    #==============================BUTTON WIDGETS=================================
    btn_register = Button(Form, text="Register User", width=45, command=RegisterUser)
    btn_register.grid(pady=25, row=6, columnspan=2)
    btn_register.bind('<Return>', RegisterUser)
    btn_login = Button(Form, text="Already registered click here..", width=45, command=HomeWindow)
    btn_login.grid(pady=25, row=7, columnspan=2)
    btn_login.bind('<Return>', HomeWindow)

    root.mainloop()


