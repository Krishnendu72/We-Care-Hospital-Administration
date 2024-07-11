from tkinter import *
import tkinter.messagebox
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lights@123",
    database="HMS"
)

cursor = conn.cursor()
print("DATABASE CONNECTION SUCCESSFUL")

class dept:
    def __init__(self, master,main_window):
        self.master = master
        self.main_window = main_window
        self.master.title("WE CARE HOSPITAL ADMINISTRATION")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        # Attributes
        #self.dep_ID = StringVar()
        self.dep_name = StringVar()
        self.dep_head = StringVar()
        self.dep_fund = StringVar()

        # Title
        self.lblTitle = Label(self.frame, text="DEPARTMENT REGISTRATION FORM", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        # Frame 1
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        # Frame 2
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        # Labels and Entries
        #self.lbldepid = Label(self.LoginFrame, text="DEPARTMENT ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        #self.lbldepid.grid(row=0, column=0)
        #self.lbldpid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.dep_ID)
        #self.lbldpid.grid(row=0, column=1)

        self.lbldepname = Label(self.LoginFrame, text="DEPARTMENT NAME", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldepname.grid(row=1, column=0)
        self.lbldpname = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.dep_name)
        self.lbldpname.grid(row=1, column=1)

        self.lbldephead = Label(self.LoginFrame, text="DEPARTMENT HEAD", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldephead.grid(row=2, column=0)
        self.lbldphead = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.dep_head)
        self.lbldphead.grid(row=2, column=1)

        self.lbldepfund = Label(self.LoginFrame, text="DEPARTMENT FUND", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldepfund.grid(row=3, column=0)
        self.lbldpfund = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.dep_fund)
        self.lbldpfund.grid(row=3, column=1)

        # Buttons
        self.button2 = Button(self.LoginFrame2, text="SAVE", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.INSERT_DEP)
        self.button2.grid(row=3, column=1)

        self.button3 = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.DELETE_DEP_DISPLAY)
        self.button3.grid(row=3, column=2)

        self.button4 = Button(self.LoginFrame2, text="UPDATE", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.UPDATE_DEP_DISPLAY)
        self.button4.grid(row=3, column=3)

        self.button6 = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.Exit)
        self.button6.grid(row=3, column=4)

    def Exit(self):
        self.master.destroy()
        self.main_window.deiconify()

    def INSERT_DEP(self):
        global d1, d2, d3, d4

        
        d2 = self.dep_name.get().capitalize()
        d4 = self.dep_head.get()
        d3 = self.dep_fund.get()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Lights@123",
            database="HMS"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM department WHERE DEPARTMENT_NAME = %s", (d2,))
        p = cursor.fetchall()
        x = len(p)

        if x != 0:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "DEPARTMENT ID ALREADY EXISTS")
        else:
            cursor.execute("INSERT INTO department (DEPARTMENT_NAME,DEPARTMENT_FUND,DEPARTMENT_HEAD) VALUES (%s, %s, %s)", (d2, d3, d4))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DEPARTMENT DATA ADDED")

        conn.commit()

    def DELETE_DEP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = D_DEP(self.newWindow)

    def UPDATE_DEP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = U_DEP(self.newWindow)

class U_DEP:

    def __init__(self, master):
        self.master = master
        self.master.title("WE CARE HOSPITAL ADMINISTRATION")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        # Attributes
        self.dep_ID = StringVar()
        self.dep_name = StringVar()
        self.dep_head = StringVar()
        self.dep_fund = StringVar()

        # Title
        self.lblTitle = Label(self.frame, text="DEPARTMENT REGISTRATION FORM", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        # Frame 1
        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        # Frame 2
        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        # Labels and Entries
        self.lbldepid = Label(self.LoginFrame, text="DEPARTMENT ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldepid.grid(row=0, column=0)
        self.lbldpid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.dep_ID)
        self.lbldpid.grid(row=0, column=1)

        self.lbldepname = Label(self.LoginFrame, text="DEPARTMENT NAME", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldepname.grid(row=1, column=0)
        self.lbldpname = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.dep_name)
        self.lbldpname.grid(row=1, column=1)

        self.lbldephead = Label(self.LoginFrame, text="DEPARTMENT HEAD", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldephead.grid(row=2, column=0)
        self.lbldphead = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.dep_head)
        self.lbldphead.grid(row=2, column=1)

        self.lbldepfund = Label(self.LoginFrame, text="DEPARTMENT FUND", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldepfund.grid(row=3, column=0)
        self.lbldpfund = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.dep_fund)
        self.lbldpfund.grid(row=3, column=1)

        # Buttons
        
        self.button4 = Button(self.LoginFrame2, text="UPDATE", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.UPDATE)
        self.button4.grid(row=3, column=1)

        self.button6 = Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.Exit)
        self.button6.grid(row=3, column=2)

    def Exit(self):
        self.master.destroy()

    def UPDATE(self):
        global d1, d2, d3, d4

        d1 = self.dep_ID.get()
        d2 = self.dep_name.get().capitalize()
        d4 = self.dep_head.get()
        d3 = self.dep_fund.get()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Lights@123",
            database="HMS"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM department WHERE DEP_ID = %s", (d1,))
        p = cursor.fetchall()
        x = len(p)

        if x == 0:
            tkinter.messagebox.showerror("WE CARE HOSPITAL ADMINISTRATION", "DEPARTMENT DOES NOT EXISTS")
        else:
            cursor.execute("UPDATE department SET DEPARTMENT_NAME = %s ,DEPARTMENT_FUND = %s ,DEPARTMENT_HEAD =  %s WHERE DEPT_ID = %s)", (d2, d3, d4,d1))
            tkinter.messagebox.showinfo("WE CARE HOSPITAL ADMINISTRATION", "DEPARTMENT DATA UPDATED")

        conn.commit()


class D_DEP:
    def __init__(self, master):
        self.master = master
        self.master.title("WE CARE HOSPITAL ADMINISTRATION")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        self.de1_dep = StringVar()

        self.lblTitle = Label(self.frame, text="DELETE DEPARTMENT WINDOW", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        self.LoginFrame = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        self.LoginFrame2 = Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        self.lbldepid = Label(self.LoginFrame, text="ENTER DEPARTMENT ID TO DELETE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldepid.grid(row=0, column=0)
        self.lbldpid = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.de1_dep)
        self.lbldpid.grid(row=0, column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.DELETE_DEP)
        self.DeleteB.grid(row=3, column=1)

    def DELETE_DEP(self):
        global inp_d_dep
        inp_d_dep = str(self.de1_dep.get())

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Lights@123",
            database="HMS"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM department WHERE DEPT_ID = %s", (inp_d_dep,))
        p = cursor.fetchall()

        if len(p) != 0:
            cursor.execute("DELETE FROM department WHERE DEPT_ID = %s", (inp_d_dep,))
            tkinter.messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DEPARTMENT DATA DELETED")
        else:
            tkinter.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "DEPARTMENT DATA DOESN'T EXIST")

        conn.commit()

