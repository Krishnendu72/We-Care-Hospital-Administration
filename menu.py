import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

# Import your forms for Patient, Room, Employee, Appointment, and Billing
from patient_form import Patient
from room_form import Room
from employee_form import Employee
from appointment_form import Appointment
from billing_form import Billing
from record_win import Record
from department_form import dept

# Establish database connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="HMS"
)

print("DATABASE CONNECTION SUCCESSFUL")

#root=Tk()

class Menu:
    def __init__(self, master,main_window):
        self.master = master
        self.main_window = main_window
        self.master.title("WE CARE HOSPITAL ADMINISTRATION")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = tk.Frame(self.master, bg="cadet blue")
        self.frame.pack()

        self.lblTitle = tk.Label(self.frame, text="MAIN MENU", font=("Helvetica", 20, "bold"), bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=50)

        self.LoginFrame = tk.Frame(self.frame, width=400, height=80, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0)

        buttons = [
            ("1. PATIENT REGISTRATION", self.Patient_Reg),
            ("2. ROOM ALLOCATION", self.Room_Allocation),
            ("3. EMPLOYEE REGISTRATION", self.Employee_Reg),
            ("4. BOOK APPOINTMENT", self.Appointment_Form),
            ("5. PATIENT BILL", self.Billing_Form),
            ("6. VIEW RECORDS", self.View_Records),
            ("7. DEPARTMENT REGISTRATION", self.Department_Reg),
            ("8. EXIT", self.Exit)
        ]

        for i, (text, command) in enumerate(buttons):
            button = tk.Button(self.LoginFrame, text=text, width=30, font=("Helvetica", 14, "bold"), bg="cadet blue", command=command)
            button.grid(row=i, column=0, pady=10)

    def Exit(self):
        self.master.destroy()
        self.main_window.deiconify()

    def Patient_Reg(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Patient(self.newWindow,self.master)
        self.master.withdraw()

    def Room_Allocation(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Room(self.newWindow,self.master)
        self.master.withdraw()

    def Employee_Reg(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Employee(self.newWindow,self.master)
        self.master.withdraw()

    def Appointment_Form(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Appointment(self.newWindow,self.master)
        self.master.withdraw()

    def Billing_Form(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Billing(self.newWindow,self.master)
        self.master.withdraw()

    def View_Records(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = Record(self.newWindow,self.master)
        self.master.withdraw()

    def Department_Reg(self):
        self.newWindow = tk.Toplevel(self.master)
        self.app = dept(self.newWindow,self.master)
        self.master.withdraw()

#root.mainloop()
