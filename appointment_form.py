from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
import mysql.connector
from mysql.connector import Error
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database = "HMS"
)
#root = Tk()
cursor=conn.cursor()
print("DATABASE CONNECTION SUCCESSFUL")
class Appointment:
    def __init__(self,master,main_window):
        self.master = master
        self.main_window = main_window
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()

        #=============ATTRIBUTES===========
        
        self.pat_ID=IntVar()
        self.emp_ID=StringVar()
        self.ap_no=StringVar()
        self.ap_time=StringVar()
        self.ap_date=StringVar()
        self.des=StringVar()

        #===============TITLE==========
        self.lblTitle = Label(self.frame,text = "APPOINTMENT FORM", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpid = Label(self.LoginFrame,text="PATIENT ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpid.grid(row=0,column=0)
        self.lblpid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.pat_ID)
        self.lblpid.grid(row=0,column=1)
        
        self.lbldid = Label(self.LoginFrame,text="DOCTOR ID",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldid.grid(row=1,column=0)
        self.lbldid  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.emp_ID )
        self.lbldid.grid(row=1,column=1)
            
        self.lblapt = Label(self.LoginFrame,text="APPOINTMENT TIME(HH:MM:SS)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapt.grid(row=0,column=2)
        self.lblapt  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.ap_time )
        self.lblapt.grid(row=0,column=3)

        self.lblapd = Label(self.LoginFrame,text="APPOINTMENT DATE(YYYY-MM-DD)",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblapd.grid(row=1,column=2)
        self.lblapd  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.ap_date)
        self.lblapd.grid(row=1,column=3)
        
        self.lbldes = Label(self.LoginFrame,text="DESCRIPTION",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lbldes.grid(row=2,column=1)
        self.lbldes  = Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable=self.des)
        self.lbldes.grid(row=2,column=2)
        

        self.button2 = Button(self.LoginFrame2, text="SAVE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.INSERT_AP)
        self.button2.grid(row=3,column=1)
        
        self.button3 = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command= self.DE_AP_DISPLAY)
        self.button3.grid(row=3,column=2)
        
        
        self.button3 = Button(self.LoginFrame2, text="SEARCH APPOINTMENTS",width =20,font="Helvetica 14 bold",bg="cadet blue",command= self.S_AP_DISPLAY)
        self.button3.grid(row=3,column=3)
     
        self.button6 = Button(self.LoginFrame2, text="EXIT",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.Exit)
        self.button6.grid(row=3,column=4)

    def Exit(self):            
        self.master.destroy()
        self.main_window.deiconify()

    def INSERT_AP(self):
        global e1, e2, e3, e4, e5, e6

        e2 = self.emp_ID.get()
        e3 = self.pat_ID.get()
        e4 = self.ap_time.get()
        e5 = self.ap_date.get()
        e6 = self.des.get()

        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="HMS"
            )
            cursor = conn.cursor()

            cursor.execute(
                "SELECT AP_NO FROM appointment WHERE AP_DATE = %s AND PATIENT_ID = %s AND EMP_ID = %s AND AP_TIME = %s", 
                (e5, e3, e2, e4)
            )
            e1 = cursor.fetchall()

            if e1:  # Check if the appointment exists
                Tk.messagebox.showerror("HOSPITAL DATABASE SYSTEM", "APPOINTMENT ALREADY EXISTS")
            else:
                cursor.execute(
                    "INSERT INTO appointment (PATIENT_ID, EMP_ID, AP_DATE, AP_TIME, DESCRIPTION) VALUES (%s, %s, %s, %s, %s)", 
                    (e3, e2, e5, e4, e6)
                )
                messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "APPOINTMENT SET SUCCESSFULLY")

            conn.commit()

        except Error as e:
            messagebox.showerror("HOSPITAL DATABASE SYSTEM", f"Error: {e}")

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def DE_AP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = DEL_AP(self.newWindow)

    def S_AP_DISPLAY(self):
        self.newWindow = Toplevel(self.master)
        self.app = SEA_AP(self.newWindow)
           
     
class DEL_AP:
    def __init__(self,master):    
        global de1_ap,de
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master,bg="cadet blue")
        self.frame.pack()
        self.de1_ap=StringVar()
        self.lblTitle = Label(self.frame,text = "DELETE APPOINTMENT WINDOW", font="Helvetica 20 bold",bg="cadet blue")
        self.lblTitle.grid(row =0 ,column = 0,columnspan=2,pady=50)
        #==============FRAME==========
        self.LoginFrame = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame.grid(row=1,column=0)
        self.LoginFrame2 = Frame(self.frame,width=400,height=80,relief="ridge",bg="cadet blue",bd=20)
        self.LoginFrame2.grid(row=2,column=0)
        #===========LABELS=============          
        self.lblpatid = Label(self.LoginFrame,text="ENTER APPOINTMENT NO TO DELETE",font="Helvetica 14 bold",bg="cadet blue",bd=22)
        self.lblpatid.grid(row=0,column=0)
        self.lblpatid= Entry(self.LoginFrame,font="Helvetica 14 bold",bd=2,textvariable= self.de1_ap)
        self.lblpatid.grid(row=0,column=1)

        self.DeleteB = Button(self.LoginFrame2, text="DELETE",width =10,font="Helvetica 14 bold",bg="cadet blue",command = self.DELETE_AP)
        self.DeleteB.grid(row=3,column=1)
        
    def DELETE_AP(self):
        global inp_d
        inp_d = str(self.de1_ap.get())
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database = "HMS"
        )
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM appointment WHERE AP_NO = %s", (inp_d,))
        v = cursor.fetchall()

        if len(v) == 0:
            messagebox.showerror("HOSPITAL DATABASE SYSTEM", "PATIENT APPOINTMENT NOT FIXED")
        else:
            cursor.execute('DELETE FROM APPOINTMENT WHERE AP_NO = %s', (inp_d,))
            messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "PATIENT APPOINTMENT DELETED")

        conn.commit()


class SEA_AP:
    def __init__(self, master):    
        self.master = master
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        self.entry = StringVar()
        self.lblTitle = Label(self.frame, text="SEARCH APPOINTMENT WINDOW", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=2, pady=25)

        self.LoginFrame = Frame(self.frame, width=800, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0, pady=20)

        self.lblpatid = Label(self.LoginFrame, text="ENTER DATE TO VIEW APPOINTMENTS (YYYY-MM-DD)", font="Helvetica 14 bold", bg="cadet blue", bd=10)
        self.lblpatid.grid(row=0, column=0, padx=20, pady=10)

        self.entry_field = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.entry, width=20)
        self.entry_field.grid(row=0, column=1, padx=20, pady=10)

        self.SearchB = Button(self.LoginFrame, text="SEARCH", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.SEARCH_AP)
        self.SearchB.grid(row=0, column=2, padx=20, pady=10)

    def SEARCH_AP(self):
        ap_date = self.entry.get()

        c1 = conn.cursor()

        c1.execute("SELECT * FROM appointment WHERE AP_DATE = %s", (ap_date,))
        appointments = c1.fetchall()

        if len(appointments) == 0:
            messagebox.showerror("HOSPITAL DATABASE SYSTEM", "NO APPOINTMENT FOR TODAY")
        else:
            c1.execute('''
                SELECT p.PATIENT_ID, p.NAME AS PATIENT_NAME, a.AP_NO, a.EMP_ID, a.AP_DATE, a.AP_TIME, e.EMP_NAME AS DOCTOR_NAME
                FROM PATIENT p 
                INNER JOIN appointment a ON p.PATIENT_ID = a.PATIENT_ID 
                INNER JOIN employee e ON a.EMP_ID = e.EMP_ID 
                WHERE a.AP_DATE = %s
            ''', (ap_date,))
            appointments_details = c1.fetchall()

            # Clear previous entries in the frame
            for widget in self.LoginFrame.winfo_children():
                widget.destroy()

            # Labels for appointment details
            labels = ["PATIENT ID", "PATIENT NAME", "APPOINTMENT NO", "DOCTOR ID", "DOCTOR NAME", "APPOINTMENT DATE", "APPOINTMENT TIME"]
            for index, label_text in enumerate(labels):
                label = Label(self.LoginFrame, text=label_text, font="Helvetica 14 bold", bg="cadet blue", bd=10)
                label.grid(row=0, column=index, padx=20, pady=10)

            # Display appointment details
            for index, appointment in enumerate(appointments_details):
                patient_id = Label(self.LoginFrame, text=appointment[0], font="Helvetica 14", bg="cadet blue", bd=2)
                patient_id.grid(row=index + 1, column=0, padx=20, pady=10)

                patient_name = Label(self.LoginFrame, text=appointment[1], font="Helvetica 14", bg="cadet blue", bd=2)
                patient_name.grid(row=index + 1, column=1, padx=20, pady=10)

                ap_no = Label(self.LoginFrame, text=appointment[2], font="Helvetica 14", bg="cadet blue", bd=2)
                ap_no.grid(row=index + 1, column=2, padx=20, pady=10)

                doctor_id = Label(self.LoginFrame, text=appointment[3], font="Helvetica 14", bg="cadet blue", bd=2)
                doctor_id.grid(row=index + 1, column=3, padx=20, pady=10)

                doctor_name = Label(self.LoginFrame, text=appointment[6], font="Helvetica 14", bg="cadet blue", bd=2)
                doctor_name.grid(row=index + 1, column=4, padx=20, pady=10)

                ap_date = Label(self.LoginFrame, text=appointment[4], font="Helvetica 14", bg="cadet blue", bd=2)
                ap_date.grid(row=index + 1, column=5, padx=20, pady=10)

                ap_time = Label(self.LoginFrame, text=appointment[5], font="Helvetica 14", bg="cadet blue", bd=2)
                ap_time.grid(row=index + 1, column=6, padx=20, pady=10)

#root.mainloop()

