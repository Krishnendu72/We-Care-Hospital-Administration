import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import ttk, messagebox

class Billing:
    def __init__(self, master, main_window):
        self.master = master
        self.main_window = main_window
        self.master.title("HOSPITAL MANAGEMENT SYSTEM")
        self.master.geometry("1600x1000+0+0")
        self.master.config(bg="cadet blue")
        self.frame = Frame(self.master, bg="cadet blue")
        self.frame.pack()

        self.initialize_variables()
        self.create_widgets()

    def initialize_variables(self):
        self.P_id = IntVar()
        self.dd = StringVar()
        self.treat_1 = StringVar()
        self.treat_2 = StringVar()
        self.cost_t = IntVar()
        self.med = StringVar()
        self.med_q = IntVar()
        self.price = DoubleVar()
        self.D_id = IntVar()  # New variable for DOC_ID

    def create_widgets(self):
        self.lblTitle = Label(self.frame, text="BILLING WINDOW", font="Helvetica 20 bold", bg="cadet blue")
        self.lblTitle.grid(row=0, column=0, columnspan=4, pady=25)

        self.LoginFrame = Frame(self.frame, width=800, height=400, relief="ridge", bg="cadet blue", bd=20)
        self.LoginFrame.grid(row=1, column=0, padx=50, pady=20)

        self.lblpid = Label(self.LoginFrame, text="PATIENT ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblpid.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.lblpid_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.P_id)
        self.lblpid_entry.grid(row=0, column=1, padx=10, pady=10)

        self.lbldocid = Label(self.LoginFrame, text="DOCTOR ID", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldocid.grid(row=0, column=2, padx=10, pady=10, sticky='w')

        self.lbldocid_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.D_id)
        self.lbldocid_entry.grid(row=0, column=3, padx=10, pady=10)

        self.lbldid = Label(self.LoginFrame, text="DATE DISCHARGED (if) (YYYY-MM-DD)", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbldid.grid(row=1, column=0, padx=10, pady=10, sticky='w')

        self.lbldid_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.dd)
        self.lbldid_entry.grid(row=1, column=1, padx=10, pady=10)

        self.button2 = Button(self.LoginFrame, text="UPDATE DISCHARGE DATE", width=25, font="Helvetica 14 bold", bg="cadet blue", command=self.UPDATE_DATE)
        self.button2.grid(row=1, column=2, padx=10, pady=10)

        self.lbltreat = Label(self.LoginFrame, text="TREATMENT", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lbltreat.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        self.lbltreat_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.treat_1)
        self.lbltreat_entry.grid(row=2, column=1, padx=10, pady=10)

        self.lblcode_t1 = Label(self.LoginFrame, text="TREATMENT CODE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblcode_t1.grid(row=3, column=0, padx=10, pady=10, sticky='w')

        self.lblcode_t1_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.treat_2)
        self.lblcode_t1_entry.grid(row=3, column=1, padx=10, pady=10)

        self.lblap = Label(self.LoginFrame, text="TREATMENT COST ₹", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblap.grid(row=4, column=0, padx=10, pady=10, sticky='w')

        self.lblap_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.cost_t)
        self.lblap_entry.grid(row=4, column=1, padx=10, pady=10)

        self.lblmed = Label(self.LoginFrame, text="MEDICINE", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblmed.grid(row=2, column=2, padx=10, pady=10, sticky='w')

        self.lblmed_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.med)
        self.lblmed_entry.grid(row=2, column=3, padx=10, pady=10)

        self.med_t1 = Label(self.LoginFrame, text="MEDICINE QUANTITY", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.med_t1.grid(row=3, column=2, padx=10, pady=10, sticky='w')

        self.med_t1_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.med_q)
        self.med_t1_entry.grid(row=3, column=3, padx=10, pady=10)

        self.lblapd = Label(self.LoginFrame, text="MEDICINE PRICE ₹", font="Helvetica 14 bold", bg="cadet blue", bd=22)
        self.lblapd.grid(row=4, column=2, padx=10, pady=10, sticky='w')

        self.lblapd_entry = Entry(self.LoginFrame, font="Helvetica 14 bold", bd=2, textvariable=self.price)
        self.lblapd_entry.grid(row=4, column=3, padx=10, pady=10)

        self.button3 = Button(self.LoginFrame, text="SUBMIT DATA", width=15, font="Helvetica 14 bold", bg="cadet blue", command=self.UPDATE_DATA)
        self.button3.grid(row=5, column=0, padx=10, pady=10)

        self.button4 = Button(self.LoginFrame, text="ADD MEDICINE", width=15, font="Helvetica 14 bold", bg="cadet blue", command=self.ADD_MEDICINE)
        self.button4.grid(row=5, column=1, padx=10, pady=10)

        self.button5 = Button(self.LoginFrame, text="GENERATE BILL", width=15, font="Helvetica 14 bold", bg="cadet blue", command=self.GEN_BILL)
        self.button5.grid(row=5, column=2, padx=10, pady=10)

        self.button6 = Button(self.LoginFrame, text="EXIT", width=10, font="Helvetica 14 bold", bg="cadet blue", command=self.Exit)
        self.button6.grid(row=5, column=3, padx=10, pady=10)

        self.listbox = Listbox(self.frame, width=100, height=5, font=("Helvetica", 12))
        self.listbox.grid(row=2, column=0, columnspan=4, padx=50, pady=20)

    def Exit(self):
        self.master.destroy()
        self.main_window.deiconify()

    def db_connect(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="HMS"
            )
            return conn
        except mysql.connector.Error as e:
            messagebox.showerror("Database Error", f"Error connecting to MySQL database:\n{e}")
            return None

    def UPDATE_DATE(self):
        b1 = self.P_id.get()
        b2 = self.dd.get()
        conn = self.db_connect()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute("UPDATE ROOM SET DATE_DISCHARGED=%s WHERE PATIENT_ID=%s", (b2, b1))
                messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "DISCHARGE DATE UPDATED")
                conn.commit()
                cursor.close()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"MySQL Error: {e}")
            finally:
                conn.close()

    def UPDATE_DATA(self):
        b1 = self.P_id.get()
        b2 = self.D_id.get()
        b3 = self.treat_1.get()
        b4 = self.treat_2.get()
        b5 = self.cost_t.get()

        conn = self.db_connect()
        if conn:
            c1 = conn.cursor()
            try:
                c1.execute("SELECT * FROM CONSULT WHERE PATIENT_ID=%s AND EMP_ID = %s", (b1,b2))
                p = c1.fetchall()
                if len(p) == 0:
                    c1.execute("INSERT INTO CONSULT (PATIENT_ID, EMP_ID) VALUES (%s, %s)",
                               (b1, b2))
                    conn.commit()
                    messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "CONSULT DATA SAVED")

                c1.execute("INSERT INTO TREATMENT (PATIENT_ID, DOC_ID, TREATMENT, TREATMENT_CODE, T_COST) VALUES (%s, %s, %s, %s, %s)", 
                           (b1, b2, b3, b4, b5))
                conn.commit()

                # Insert medicines into MEDICINE table
                medicine_list = self.listbox.get(0, END)
                for item in medicine_list:
                    parts = item.split(" - ")
                    med_name = parts[0]
                    quantity = int(parts[1].split()[0])
                    price = float(parts[2][1:])

                    try:
                        # Insert into MEDICINE table
                        c1.execute("INSERT INTO MEDICINE (PATIENT_ID, MEDICINE_NAME, M_QTY, M_COST) VALUES (%s, %s, %s, %s)", 
                                   (b1, med_name, quantity, price))
                        conn.commit()
                    except mysql.connector.Error as err:
                        messagebox.showerror("HOSPITAL DATABASE SYSTEM", f"MySQL Error: {err}")

                messagebox.showinfo("HOSPITAL DATABASE SYSTEM", "BILLING DATA SAVED")
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"MySQL Error: {e}")
            finally:
                c1.close()
                conn.close()

    def ADD_MEDICINE(self):
        price = 0
        med_name = self.med.get()
        med_quantity = self.med_q.get()
        med_price = self.price.get()
        price += med_price
        if med_name and med_quantity and med_price:
            item = f"{med_name} - {med_quantity} units - ₹{med_price:.2f}"
            self.listbox.insert(END, item)
        else:
            messagebox.showerror("Error", "Please enter all fields for medicine.")

    def GEN_BILL(self):
        b1 = self.P_id.get()
        conn = self.db_connect()
        if conn:
            try:
                rate = 0
                cursor = conn.cursor()

                # Fetch room rate for the patient
                
                cursor.execute("SELECT RATE * (DATEDIFF(DATE_DISCHARGED, DATE_ADMITTED)) FROM ROOM WHERE PATIENT_ID = %s AND PAY_STATUS = 'NO'", (b1,))
                room_data = cursor.fetchone()
            
                if room_data:
                    rate = room_data[0]

                # Calculate total amount including treatment and medicine costs
                #billing only at the end of the day
                cursor.execute("SELECT T_COST FROM TREATMENT WHERE PATIENT_ID = %s AND DATE(T_DATE) = CURRENT_DATE ORDER BY T_DATE DESC LIMIT 1", (b1,))
                treatment_cost_data = cursor.fetchone()
                treatment_cost = treatment_cost_data[0] if treatment_cost_data[0] else 0

                cursor.execute("SELECT SUM(M_COST * M_QTY) FROM MEDICINE WHERE PATIENT_ID = %s AND DATE(M_DATE) = CURRENT_DATE ", (b1,))
                medicine_cost_data = cursor.fetchone()
                medicine_cost = medicine_cost_data[0] if medicine_cost_data[0] else 0

                total_amount = treatment_cost + rate + medicine_cost

                cursor.execute("INSERT INTO BILL (PATIENT_ID, BILL) VALUES (%s, %s)", (b1, total_amount))

                # Display total amount in listbox
                self.listbox.delete(0, END)
                self.listbox.insert(END, f"Total Amount: ₹{total_amount:.2f}")

                if rate != 0:
                    cursor.execute("UPDATE ROOM SET PAY_STATUS = 'YES' WHERE PATIENT_ID = %s", (b1,))
                    messagebox.showinfo("HOSPITAL MANAGEMENT", "TOTAL AMOUNT INCLUDES ROOM CHARGES")

                conn.commit()
            except mysql.connector.Error as e:
                messagebox.showerror("Database Error", f"MySQL Error: {e}")
            finally:
                cursor.close()
                conn.close()

