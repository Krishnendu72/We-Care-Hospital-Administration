from sqlite3 import Cursor
import tkinter as tk
from tkinter import messagebox
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="HMS"
)

class Employee:
    def __init__(self, master,main_window):
        self.master = master
        self.main_window = main_window
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = tk.Frame(self.master, bg="cadet blue")
        self.frame.pack()

        # Attributes
        self.emp_name = tk.StringVar()
        self.emp_sex = tk.StringVar()
        self.emp_age = tk.IntVar()
        self.emp_type = tk.StringVar()
        self.emp_salary = tk.IntVar()
        self.emp_exp = tk.StringVar()
        self.emp_email = tk.StringVar()
        self.emp_phno = tk.StringVar()  # Use StringVar to validate length

        # Title
        self.lblTitle = tk.Label(self.frame, text="EMPLOYEE REGISTRATION FORM", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        # Frame
        self.LoginFrame = tk.Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        self.LoginFrame2 = tk.Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)

        # Labels and Entries
        self.lblempname = tk.Label(self.LoginFrame, text="EMPLOYEE NAME", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblempname.grid(row=0, column=0)
        self.lblempname_entry = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_name)
        self.lblempname_entry.grid(row=0, column=1)

        self.lblsex = tk.Label(self.LoginFrame, text="SEX", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblsex.grid(row=1, column=0)
        self.lblsex_entry = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_sex)
        self.lblsex_entry.grid(row=1, column=1)

        self.lblage = tk.Label(self.LoginFrame, text="AGE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblage.grid(row=2, column=0)
        self.lblage_entry = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_age)
        self.lblage_entry.grid(row=2, column=1)

        self.lbltype = tk.Label(self.LoginFrame, text="EMPLOYEE DESIGNATION [DOCTOR, NURSE, RECEPTIONIST]", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbltype.grid(row=3, column=0)
        self.lbltype_entry = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_type)
        self.lbltype_entry.grid(row=3, column=1)

        self.lblsalary = tk.Label(self.LoginFrame, text="SALARY", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblsalary.grid(row=0, column=2)
        self.lblsalary_entry = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_salary)
        self.lblsalary_entry.grid(row=0, column=3)

        self.lblexp = tk.Label(self.LoginFrame, text="EXPERIENCE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblexp.grid(row=1, column=2)
        self.lblexp_entry = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_exp)
        self.lblexp_entry.grid(row=1, column=3)

        self.lblphno = tk.Label(self.LoginFrame, text="CONTACT NUMBER", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblphno.grid(row=2, column=2)
        self.lblphno_entry = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_phno)
        self.lblphno_entry.grid(row=2, column=3)

        self.lblemail = tk.Label(self.LoginFrame, text="EMAIL", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblemail.grid(row=3, column=2)
        self.lblemail_entry = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_email)
        self.lblemail_entry.grid(row=3, column=3)

        self.button2 = tk.Button(self.LoginFrame2, text="SUBMIT", width=10, font="Helvetica 14 bold", bg="cadet blue", command=lambda: self.INSERT_EMP(self.get_emp_data()))
        self.button2.grid(row=0, column=1)
        
        self.button3 = tk.Button(self.LoginFrame2, text="UPDATE", width=10, font="Helvetica 14 bold", bg="cadet blue", command=lambda: self.UPDATE_EMP(self.get_emp_data()))
        self.button3.grid(row=0, column=2)
        
        self.button4 = tk.Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.DE_DISPLAY)
        self.button4.grid(row=0, column=3)
        
        self.button5 = tk.Button(self.LoginFrame2, text="SEARCH", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.S_DISPLAY)
        self.button5.grid(row=0, column=4)
        
        self.button6 = tk.Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.Exit)
        self.button6.grid(row=0, column=5)

    def Exit(self):
        self.master.destroy()
        self.main_window.deiconify()

    def clear(self):
        self.lblempname_entry.delete(0, 'end')
        self.lblage_entry.delete(0, 'end')
        self.lblsex_entry.delete(0, 'end')
        self.lblemail_entry.delete(0, 'end')
        self.lblphno_entry.delete(0, 'end')
        self.lblsalary_entry.delete(0, 'end')
        self.lblexp_entry.delete(0, 'end')
        self.lbltype_entry.delete(0, 'end')
      
        # Clear the corresponding fields in the database table
        #query = "DELETE FROM your_table_name"
        #cursor.execute(query)
        conn.commit()


    def get_emp_data(self):
        return {
            "name": self.emp_name.get(),
            "sex": self.emp_sex.get(),
            "age": self.emp_age.get(),
            "type": self.emp_type.get(),
            "salary": self.emp_salary.get(),
            "exp": self.emp_exp.get(),
            "email": self.emp_email.get(),
            "phno": self.emp_phno.get()
        }
    def check_designation(self):
        if self.emp_type.get() in ["doctor", "nurse"]:
            self.newWindow = tk.Toplevel(self.master)
            self.app = Department(self.newWindow, self.get_emp_data())
        
    def DE_DISPLAY(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = D_EMP(self.newWindow)

    def S_DISPLAY(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = S_EMP(self.newWindow)

    def INSERT_EMP(self, emp_data):
        try:
            cursor = conn.cursor()

            insert_query = """
                INSERT INTO employee (EMP_NAME, SEX, AGE, DESIG, SAL, EXP, EMAIL, PHONE)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(insert_query, (emp_data['name'], emp_data['sex'], emp_data['age'], emp_data['type'],
                                          emp_data['salary'], emp_data['exp'], emp_data['email'], emp_data['phno']))
            conn.commit()

            messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA ADDED")
            self.check_designation()
            self.clear()

        except ValueError as ve:
            messagebox.showerror("Invalid Input", str(ve))
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    def UPDATE_EMP(self, emp_data):
        self.newWindow = tk.Toplevel(self.master)
        self.app = U_EMP(self.newWindow)

class U_EMP:
    def __init__(self, master):
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = tk.Frame(self.master, bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.emp_ID = tk.StringVar()
        self.emp_name = tk.StringVar()
        self.emp_sex = tk.StringVar()
        self.emp_age = tk.IntVar()
        self.emp_type = tk.StringVar()
        self.emp_salary = tk.IntVar()
        self.emp_exp = tk.StringVar()
        self.emp_email = tk.StringVar()
        self.emp_phno = tk.IntVar()

        #===============TITLE==========
        self.lblTitle = tk.Label(self.frame, text="EMPLOYEE UPDATION FORM", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)
        
        #==============FRAME==========
        self.LoginFrame = tk.Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        
        self.LoginFrame2 = tk.Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        
        #===========LABELS=============          
        self.lblempid = tk.Label(self.LoginFrame, text="EMPLOYEE ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblempid.grid(row=0, column=0)
        self.entry_empid = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_ID)
        self.entry_empid.grid(row=0, column=1)
        
        self.lblempname = tk.Label(self.LoginFrame, text="EMPLOYEE NAME", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblempname.grid(row=1, column=0)
        self.entry_empname = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_name)
        self.entry_empname.grid(row=1, column=1)

        self.lblsex = tk.Label(self.LoginFrame, text="SEX", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblsex.grid(row=2, column=0)
        self.entry_sex = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_sex)
        self.entry_sex.grid(row=2, column=1)

        self.lblage = tk.Label(self.LoginFrame, text="AGE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblage.grid(row=3, column=0)
        self.entry_age = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_age)
        self.entry_age.grid(row=3, column=1)
        
        self.lbltype = tk.Label(self.LoginFrame, text="EMPLOYEE TYPE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbltype.grid(row=4, column=0)
        self.entry_type = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_type)
        self.entry_type.grid(row=4, column=1)

        self.lblsalary = tk.Label(self.LoginFrame, text="SALARY", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblsalary.grid(row=0, column=2)
        self.entry_salary = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_salary)
        self.entry_salary.grid(row=0, column=3)
        
        self.lblexp = tk.Label(self.LoginFrame, text="EXPERIENCE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblexp.grid(row=1, column=2)
        self.entry_exp = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_exp)
        self.entry_exp.grid(row=1, column=3)
        
        self.lblphno = tk.Label(self.LoginFrame, text="CONTACT NUMBER", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblphno.grid(row=2, column=2)
        self.entry_phno = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_phno)
        self.entry_phno.grid(row=2, column=3)
        
        self.lblemail = tk.Label(self.LoginFrame, text="EMAIL", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblemail.grid(row=3, column=2)
        self.entry_email = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.emp_email)
        self.entry_email.grid(row=3, column=3)
        
        self.button3 = tk.Button(self.LoginFrame2, text="UPDATE", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.UPDATE)
        self.button3.grid(row=3, column=1)
     
        self.button6 = tk.Button(self.LoginFrame2, text="EXIT", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.Exit)
        self.button6.grid(row=3, column=2)

    def Exit(self):            
        self.master.destroy()
        
    def UPDATE(self):
        global e1, e2, e3, e4, e5, e6, e7, e8, e9

        e1 = self.emp_ID.get()
        e2 = self.emp_name.get()
        e3 = self.emp_sex.get()
        e4 = self.emp_age.get()
        e5 = self.emp_type.get()
        e6 = self.emp_salary.get()
        e7 = self.emp_exp.get()
        e8 = self.emp_email.get()
        e9 = self.emp_phno.get()

        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="HMS"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employee WHERE EMP_ID = %s", (e1,))
        p = cursor.fetchall()
        x = len(p)

        if x == 0:
            messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE ID DOES NOT EXISTS")
        else:
            cursor.execute("UPDATE employee SET emp_name=%s, sex=%s, age=%s, desig=%s, sal=%s, exp=%s, email=%s, phone=%s WHERE EMP_ID=%s", (e2, e3, e4, e5, e6, e7, e8, e9, e1))
            messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA UPDATED")

        self.clear()
        conn.commit()

    def clear(self):
        self.entry_empid.delete(0, 'end')
        self.entry_empname.delete(0, 'end')
        self.entry_sex.delete(0, 'end')
        self.entry_age.delete(0, 'end')
        self.entry_type.delete(0, 'end')
        self.entry_salary.delete(0, 'end')
        self.entry_exp.delete(0, 'end')
        self.entry_phno.delete(0, 'end')
        self.entry_email.delete(0, 'end')


class S_EMP:
    def __init__(self, master):    
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = tk.Frame(self.master, bg="cadet blue")
        self.frame.pack()
        self.de1_emp = tk.StringVar()
        
        self.lblTitle = tk.Label(self.frame, text="SEARCH EMPLOYEE WINDOW", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)
        
        self.LoginFrame = tk.Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        
        self.LoginFrame2 = tk.Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        
        self.lblpatid = tk.Label(self.LoginFrame,text="ENTER EMPLOYEE ID TO SEARCH", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.lblpatid_entry = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.de1_emp)
        self.lblpatid_entry.grid(row=0, column=1)

        self.DeleteB = tk.Button(self.LoginFrame2, text="SEARCH", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.SEARCH)
        self.DeleteB.grid(row=3, column=1)

    def SEARCH(self):
        c1 = conn.cursor()
        
        inp_s = self.de1_emp.get()

        c1.execute('SELECT * FROM employee WHERE EMP_ID = %s', (inp_s,))
        p = c1.fetchall()
        
        if len(p) == 0:
            messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE RECORD NOT FOUND")
        else:
            for i in p:
                self.l1 = tk.Label(self.LoginFrame, text="EMPLOYEE ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                self.l1.grid(row=1, column=0)
                self.dis1 = tk.Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[0])
                self.dis1.grid(row=1, column=1)

                self.l2 = tk.Label(self.LoginFrame, text="EMPLOYEE NAME", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                self.l2.grid(row=2, column=0)
                self.dis2 = tk.Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[1])
                self.dis2.grid(row=2, column=1)

                self.l3 = tk.Label(self.LoginFrame, text="SEX", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                self.l3.grid(row=3, column=0)
                self.dis3 = tk.Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[2])
                self.dis3.grid(row=3, column=1)

                self.l4 = tk.Label(self.LoginFrame, text="AGE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                self.l4.grid(row=4, column=0)
                self.dis4 = tk.Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[3])
                self.dis4.grid(row=4, column=1)

                self.l5 = tk.Label(self.LoginFrame, text="DESIGNATION", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                self.l5.grid(row=5, column=0)
                self.dis5 =tk. Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[4])
                self.dis5.grid(row=5, column=1)

                self.l6 = tk.Label(self.LoginFrame, text="SALARY", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                self.l6.grid(row=1, column=2)
                self.dis6 = tk.Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[5])
                self.dis6.grid(row=1, column=3)

                self.l7 = tk.Label(self.LoginFrame, text="EXPERIENCE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                self.l7.grid(row=2, column=2)
                self.dis7 = tk.Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[6])
                self.dis7.grid(row=2, column=3)

                self.l8 = tk.Label(self.LoginFrame, text="EMAIL", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                self.l8.grid(row=3, column=2)
                self.dis8 = tk.Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[7])
                self.dis8.grid(row=3, column=3)

                self.l9 = tk.Label(self.LoginFrame, text="CONTACT NUMBER", font="Helvetica 14 bold", bg="cadet blue", bd=22)
                self.l9.grid(row=4, column=2)
                self.dis9 = tk.Label(self.LoginFrame, font="Helvetica 14 bold", bd=2, bg="cadet blue", text=i[8])
                self.dis9.grid(row=4, column=3)

        c1.close()

class D_EMP:
    def __init__(self, master):    
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = tk.Frame(self.master, bg="cadet blue")
        self.frame.pack()
        self.de1_emp = tk.StringVar()
        
        self.lblTitle = tk.Label(self.frame, text="DELETE EMPLOYEE WINDOW", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)
        
        self.LoginFrame = tk.Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)
        
        self.LoginFrame2 = tk.Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame2.grid(row=2, column=0)
        
        self.lblpatid = tk.Label(self.LoginFrame,text="ENTER EMPLOYEE ID TO DELETE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblpatid.grid(row=0, column=0)
        self.lblpatid_entry = tk.Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.de1_emp)
        self.lblpatid_entry.grid(row=0, column=1)

        self.DeleteB = tk.Button(self.LoginFrame2, text="DELETE", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.DELETE_EMP)
        self.DeleteB.grid(row=3, column=1)

    def DELETE_EMP(self):
        inp_d = self.de1_emp.get()

        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employee WHERE EMP_ID = %s", (inp_d,))
            p = cursor.fetchall()

            if len(p) != 0:
                cursor.execute("DELETE FROM employee WHERE EMP_ID = %s", (inp_d,))
                conn.commit()
                messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DELETED")
            else:
                messagebox.showerror("HOSPITAL DATABASE SYSTEM", "EMPLOYEE DATA DOESN'T EXIST")

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")

    
class Department:
    def __init__(self, master, emp_data):
        self.master = master
        self.master.title("DEPARTMENT DETAILS")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.emp_data = emp_data

        self.frame = tk.Frame(self.master, bg="cadet blue")
        self.frame.pack()

        self.lblTitle = tk.Label(self.frame, text="DEPARTMENT DETAILS", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=20)

        self.lblDept = tk.Label(self.frame, text="Department", font="Helvetica 14 bold", bg="cadet blue", bd=10)
        self.lblDept.grid(row=1, column=0)
        self.dept_entry = tk.Entry(self.frame, font="Helvetica 14 bold", bd=2)
        self.dept_entry.grid(row=1, column=1)

        self.lblRole = tk.Label(self.frame, text="Role", font="Helvetica 14 bold", bg="cadet blue", bd=10)
        self.lblRole.grid(row=2, column=0)
        self.role_entry = tk.Entry(self.frame, font="Helvetica 14 bold", bd=2)
        self.role_entry.grid(row=2, column=1)

        self.lblWorkDetails = tk.Label(self.frame, text="shift Details", font="Helvetica 14 bold", bg="cadet blue", bd=10)
        self.lblWorkDetails.grid(row=3, column=0)
        self.work_details_entry = tk.Entry(self.frame, font="Helvetica 14 bold", bd=2)
        self.work_details_entry.grid(row=3, column=1)

        self.save_button = tk.Button(self.frame, text="SAVE", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.save_dept_details)
        self.save_button.grid(row=4, column=0, columnspan=2, pady=20)

    def save_dept_details(self):
        dept = self.dept_entry.get().capitalize()
        role = self.role_entry.get()
        work_details = self.work_details_entry.get()

        try:
            cursor = conn.cursor()

            queryget = """
            SELECT EMP_ID FROM EMPLOYEE WHERE EMP_NAME = %s AND EMAIL = %s
            """
            cursor.execute(queryget, (self.emp_data['name'], self.emp_data['email']))
            result = cursor.fetchone()[0]

             # Fetch DEPT_ID for the inserted department
            cursor.execute("SELECT DEPT_ID FROM department WHERE DEPARTMENT_NAME = %s", (dept,))
            dept = cursor.fetchone()[0]

            # Insert into department table
            insert_dept_query = """
                INSERT INTO WORKS(DEPT_ID, EMP_ID, ROLE, SHIFT_DETAILS)
                VALUES (%s, %s, %s, %s)
            """
            cursor.execute(insert_dept_query, (dept,result, role, work_details))
            conn.commit()

            messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DEPARTMENT DATA SAVED")
            self.master.destroy()

        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Error: {err}")
