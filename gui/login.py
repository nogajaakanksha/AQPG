from Tkinter import *
import sqlite3
import main
import register
import sys
import os


#==============================METHODS========================================
def Database():
    global conn, cursor
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `useraccount` (mem_id INTEGER NOT NULL PRIMARY KEY  AUTOINCREMENT, username TEXT, password TEXT)")       
    cursor.execute("SELECT * FROM `useraccount` WHERE `username` = 'admin' AND `password` = 'admin'")
    if cursor.fetchone() is None:
        cursor.execute("INSERT INTO `useraccount` (username, password) VALUES('admin', 'admin')")
        conn.commit()
    

def helloCallBack():
    root.destroy()
    main.gui()
    
def HomeWindow():
    helloCallBack()
def Register(event=None):
    root.destroy()
    register.gui() 
def Login(event=None):
    Database()
    if USERNAME.get() == "" or PASSWORD.get() == "":
        print("Please complete the required field!")
        Register()
    else:
        cursor.execute("SELECT * FROM `useraccount` WHERE `username` = ? AND `password` = ?", (USERNAME.get(), PASSWORD.get()))
        if cursor.fetchone() is not None:
            HomeWindow()
            USERNAME.set("")
            PASSWORD.set("")
            lbl_text.config(text="")
        else:
            print("Invalid username or password")
            USERNAME.set("")
            PASSWORD.set("")
            Register()
    cursor.close()
    conn.close()
def gui():    
    global root
    root = Tk()
    root.title("Login Application")
    width = 500
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)
    #==============================VARIABLES======================================
    global USERNAME,PASSWORD
    USERNAME = StringVar()
    PASSWORD = StringVar()

    #==============================FRAMES=========================================
    Top = Frame(root, bd=2,  relief=RIDGE)
    Top.pack(side=TOP, fill=X)
    Form = Frame(root, height=200)
    Form.pack(side=TOP, pady=20)

    #==============================LABELS=========================================
    lbl_title = Label(Top, text = "Login Application", font=('arial', 15))
    lbl_title.pack(fill=X)
    lbl_username = Label(Form, text = "Username:", font=('arial', 14), bd=15)
    lbl_username.grid(row=0, sticky="e")
    lbl_password = Label(Form, text = "Password:", font=('arial', 14), bd=15)
    lbl_password.grid(row=1, sticky="e")
    global lbl_text
    lbl_text = Label(Form)
    lbl_text.grid(row=2, columnspan=2)

    #==============================ENTRY WIDGETS==================================
    username = Entry(Form, textvariable=USERNAME, font=(14))
    username.grid(row=0, column=1)
    password = Entry(Form, textvariable=PASSWORD, show="*", font=(14))
    password.grid(row=1, column=1)

    #==============================BUTTON WIDGETS=================================
    btn_login = Button(Form, text="Login", width=45, command=Login)
    btn_login.grid(pady=25, row=3, columnspan=2)
    btn_login.bind('<Return>', Login)
    btn_register = Button(Form, text="Register User", width=45, height=3, command=Register)
    btn_register.grid(pady=25, row=4, columnspan=2)
    btn_register.bind('<Return>', Register)
    root.mainloop()
