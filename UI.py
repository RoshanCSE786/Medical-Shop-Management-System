# from cgitb import text
from tkinter import*
# from tkinter import font
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
# from msilib import Table
# from textwrap import fill
# from tkinter import BOTH, BOTTOM, HORIZONTAL, RIDGE, RIGHT, VERTICAL, _XYScrollCommand, messagebox


class PharmacyManagementSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Medical Shop Management System")
        self.root.geometry('1550x800+0+0')

        # ============Add Med Variable==============================

        self.addmed_var = StringVar()
        self.refMed_var = StringVar()

        # ===============main variable============================
        self.ref_var = StringVar()
        self.cmpName_var = StringVar()
        self.typeMed_var = StringVar()
        self.medName_var = StringVar()
        self.lot_var = StringVar()
        self.issuedate_var = StringVar()
        self.expdate_var = StringVar()
        self.uses_var = StringVar()
        self.sideEffect_var = StringVar()
        self.warning_var = StringVar()
        self.dosage_var = StringVar()
        self.price_var = StringVar()
        self.product_var = StringVar()

        lbltitle = Label(self.root, text="Medical Shop Management System", bd=15, relief=RIDGE, bg="blue",
                         fg="white", font=("times new roman", 50, "bold"), padx=2, pady=4)
        lbltitle.pack(side=TOP, fill=X)

        img1 = Image.open("D:/medical_shop/medi.webp")
        img1 = img1.resize((80, 80), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        b1 = Button(self.root, image=self.photoimg1, borderwidth=0)
        b1.place(x=70, y=16)

        # ==============================Data Frame===============================================
        DataFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        DataFrame.place(x=0, y=120, width=1530, height=400)

        DataFrameLeft = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Information",
                                   fg="darkgreen", font=("arial", 12, "bold"))

        DataFrameLeft.place(x=0, y=5, width=900, height=350)

        # ============================button Frame==================

        ButtonFrame = Frame(self.root, bd=15, relief=RIDGE, padx=20)
        ButtonFrame.place(x=0, y=520, width=1530, height=65)

        # ===========================Main button====================

        btnAddData = Button(ButtonFrame, command=self.add_data, text="Medicine Add", font=(
            "arial", 12, "bold"), bg="darkgreen", fg="white")
        btnAddData.grid(row=0, column=0)

        btnUpdatemed = Button(ButtonFrame, command=self.Update, text="UPDATE", font=(
            "arial", 13, "bold"), width=14, bg="darkgreen", fg="white")
        btnUpdatemed.grid(row=0, column=1)

        btnDeletemed = Button(ButtonFrame, command=self.delete, text="DELETE", font=(
            "arial", 13, "bold"), width=14, bg="red", fg="white")
        btnDeletemed.grid(row=0, column=2)

        btnRestMed = Button(ButtonFrame, command=self.reset, text="RESET", font=(
            "arial", 13, "bold"), width=14, bg="darkgreen", fg="white")
        btnRestMed.grid(row=0, column=3)

        btnExitMed = Button(ButtonFrame,command=self.ex, text="EXIT", font=(
            "arial", 13, "bold"), width=14, bg="darkgreen", fg="white")
        btnExitMed.grid(row=0, column=4)

        # ============search by======================================
        lblSearch = Label(ButtonFrame, font=("arial", 17, "bold"),
                          text="Search By", padx=2, bg="red", fg="white")
        lblSearch.grid(row=0, column=5, sticky=W)

        # =========variable===================
        self.search_var = StringVar()

        search_combo = ttk.Combobox(ButtonFrame, textvariable=self.search_var, width=12, font=(
            "arial", 17, "bold"), state="readonly")
        search_combo["values"] = ("refno", "medname", "lot")
        search_combo.grid(row=0, column=6)
        search_combo.current(0)

        self.serchTxt_var = StringVar()
        txtSearch = Entry(ButtonFrame, textvariable=self.serchTxt_var, bd=3, relief=RIDGE,
                          width=12, font=("arial", 17, "bold"))
        txtSearch.grid(row=0, column=7)

        searchBtn = Button(ButtonFrame,command=self.search_data, text="Search", font=(
            "arial", 13, "bold"), width=13, bg="darkgreen", fg="white")
        searchBtn.grid(row=0, column=8)

        showAll = Button(ButtonFrame, command=self.fatch_data, text="Show All", font=(
            "arial", 13, "bold"), width=13, bg="darkgreen", fg="white")
        showAll.grid(row=0, column=9)

        # ========================label and entry==========================

        lblrefno = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Reference No", padx=2)
        lblrefno.grid(row=0, column=0, sticky=W)

        conn = mysql.connector.connect(
            host="localhost", username="root", password="Roshan@01", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select Ref from pharma")
        row = my_cursor.fetchall()

        ref_combo = ttk.Combobox(DataFrameLeft, textvariable=self.ref_var, width=27, font=(
            "arial", 12, "bold"), state="readonly")
        if row:
            ref_combo["values"] = row
            ref_combo.current(0)
        ref_combo.grid(row=0, column=1)

        lblCmpName = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Company Name", padx=2, pady=6)
        lblCmpName.grid(row=1, column=0, sticky=W)
        txtCmpName = Entry(DataFrameLeft, textvariable=self.cmpName_var, font=(
            "arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtCmpName.grid(row=1, column=1)

        lblTypeofMedicine = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Type of Medicine", padx=2, pady=6)
        lblTypeofMedicine.grid(row=2, column=0, sticky=W)

        comTypeofMedicine = ttk.Combobox(
            DataFrameLeft, textvariable=self.typeMed_var, state="readonly", font=("arial", 12, "bold"), width=27)
        comTypeofMedicine["value"] = (
            "Tablets", "Liquid", "Capsules", "Topical Medicine", "Drops", "Inhales", "Injection")
        comTypeofMedicine.current(0)
        comTypeofMedicine.grid(row=2, column=1)

        # ======================Add Medicine======================

        lblMedicineName = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Medicine Name", padx=2, pady=6)
        lblMedicineName.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(
            host="localhost", username="root", password="Roshan@01", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select MedName from pharma")
        med = my_cursor.fetchall()

        comMedicineName = ttk.Combobox(
            DataFrameLeft, textvariable=self.medName_var, state="readonly", font=("arial", 12, "bold"), width=27)
        if med:
            comMedicineName["value"] = med
            comMedicineName.current(0)
        comMedicineName.grid(row=3, column=1)

        lblLotNo = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Lot No", padx=2, pady=6)
        lblLotNo.grid(row=4, column=0, sticky=W)
        txtLotNo = Entry(DataFrameLeft, textvariable=self.lot_var, font=("arial", 13, "bold"),
                         bg="white", bd=2, relief=RIDGE, width=29)
        txtLotNo.grid(row=4, column=1)

        lblIssueDate = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Issue Date", padx=2, pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataFrameLeft, textvariable=self.issuedate_var, font=(
            "arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtIssueDate.grid(row=5, column=1)

        lblExDate = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Expiry Date", padx=2, pady=6)
        lblExDate.grid(row=6, column=0, sticky=W)
        txtExDate = Entry(DataFrameLeft, textvariable=self.expdate_var, font=(
            "arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtExDate.grid(row=6, column=1)

        lblUses = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Uses", padx=2, pady=6)
        lblUses.grid(row=7, column=0, sticky=W)
        txtUses = Entry(DataFrameLeft, textvariable=self.uses_var, font=("arial", 13, "bold"),
                        bg="white", bd=2, relief=RIDGE, width=29)
        txtUses.grid(row=7, column=1)

        lblSideEffect = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Side Effect", padx=2, pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataFrameLeft, textvariable=self.sideEffect_var, font=(
            "arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtSideEffect.grid(row=8, column=1)

        lblPrecWarning = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Prescription & Warning", padx=2, pady=6)
        lblPrecWarning.grid(row=0, column=2, sticky=W)
        txtPrecWarning = Entry(DataFrameLeft, textvariable=self.warning_var, font=(
            "arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtPrecWarning.grid(row=0, column=3)

        lblDosage = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="dosge", padx=2, pady=6)
        lblDosage.grid(row=1, column=2, sticky=W)
        txtDosage = Entry(DataFrameLeft, textvariable=self.dosage_var, font=(
            "arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtDosage.grid(row=1, column=3)

        lblPrice = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Tablets Price", padx=2, pady=6)
        lblPrice.grid(row=2, column=2, sticky=W)
        txtPrice = Entry(DataFrameLeft, textvariable=self.price_var, font=("arial", 13, "bold"),
                         bg="white", bd=2, relief=RIDGE, width=29)
        txtPrice.grid(row=2, column=3)

        lblProductQt = Label(DataFrameLeft, font=(
            "arial", 12, "bold"), text="Product QT", padx=2, pady=6)
        lblProductQt.grid(row=3, column=2, sticky=W)
        txtProductQt = Entry(DataFrameLeft, textvariable=self.product_var, font=(
            "arial", 13, "bold"), bg="white", bd=2, relief=RIDGE, width=29)
        txtProductQt.grid(row=3, column=3, sticky=W)

        # =====================DataFrameRight==========================

        DataFrameRight = LabelFrame(DataFrame, bd=10, relief=RIDGE, padx=20, text="Medicine Add Department",
                                    fg="darkgreen", font=("arial", 12, "bold"))

        DataFrameRight.place(x=902, y=5, width=540, height=350)

        lblreferenceno = Label(DataFrameRight, font=(
            "arial", 12, "bold"), text="Reference No")
        lblreferenceno.place(x=0, y=10)
        txtreferenceno = Entry(DataFrameRight, textvariable=self.refMed_var, font=(
            "arial", 12, "bold"), bg="white", bd=2, relief=RIDGE, width=14)
        txtreferenceno.place(x=135, y=10)

        lblmedname = Label(DataFrameRight, font=(
            "arial", 12, "bold"), text="Medicine Name")
        lblmedname.place(x=0, y=40)
        txtmedname = Entry(DataFrameRight, textvariable=self.addmed_var, font=(
            "arial", 12, "bold"), bg="white", bd=2, relief=RIDGE, width=14)
        txtmedname.place(x=135, y=40)

        # =====================Side Frame=========================================

        side_frame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="white")
        side_frame.place(x=0, y=150, width=290, height=160)

        sc_x = ttk.Scrollbar(side_frame, orient=HORIZONTAL)
        sc_x.pack(side=BOTTOM, fill=X)
        sc_y = ttk.Scrollbar(side_frame, orient=VERTICAL)
        sc_y.pack(side=RIGHT, fill=Y)

        self.medicine_table = ttk.Treeview(side_frame, columns=(
            "ref", "medname"), xscrollcommand=sc_x.set, yscrollcommand=sc_y.set)

        # sc_x.config(command=self.medicine_table.xview)
        # sc_y.config(command=self.medicine_table.yview)

        self.medicine_table.heading("ref", text="Ref")
        self.medicine_table.heading("medname", text="Medicine Name")

        self.medicine_table["show"] = "headings"
        self.medicine_table.pack(fill=BOTH, expand=1)

        self.medicine_table.column("ref", width=100)
        self.medicine_table.column("medname", width=100)

        self.medicine_table.bind("<ButtonRelease-1>", self.Medget_cursor)

        # # ====================Medicine ADD BUTTONS=====================================

        down_frame = Frame(DataFrameRight, bd=4, relief=RIDGE, bg="yelloW")
        down_frame.place(x=300, y=150, width=135, height=160)

        btnAddmed = Button(down_frame, text="ADD", font=(
            "arial", 12, "bold"), width=12, bg="lime", fg="white", pady=4, command=self.AddMed)
        btnAddmed.grid(row=0, column=0)

        btnUpdatemed = Button(down_frame, text="UPDATE", font=(
            "arial", 12, "bold"), width=12, bg="RED", fg="white", pady=4, command=self.UpdateMed)
        btnUpdatemed.grid(row=1, column=0)

        btnDeletemed = Button(down_frame, text="DELETE", font=(
            "arial", 12, "bold"), width=12, bg="PURPLE", fg="white", pady=4, command=self.DeleteMed)
        btnDeletemed.grid(row=2, column=0)

        btnClearmed = Button(down_frame, text="CLEAR", font=(
            "arial", 12, "bold"), width=12, bg="ORANGE", fg="white", pady=4, command=self.ClearMed)
        btnClearmed.grid(row=3, column=0)

        # # =====================FRAME DETAILS=====================================

        Framedetails = Frame(self.root, bd=15, relief=RIDGE)
        Framedetails.place(x=0, y=580, width=1530, height=210)

        # # ====================Main TABLE & SCROLLBAR=============================

        Table_frame = Frame(Framedetails, bd=15, relief=RIDGE, padx=20)
        Table_frame.place(x=0, y=1, width=1500, height=180)

        scroll_x = ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y = ttk.Scrollbar(Table_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)

        data1 = ("refno", "cmpName", "type",
                 "tablename", "lotno", "issuedate",
                 "expdate", "uses", "sideeffect", "warning",
                 "dosge", "price", "product")
        self.pharmacy_table = ttk.Treeview(Table_frame, column=(
            data1), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.pharmacy_table.xview)
        scroll_y.config(command=self.pharmacy_table.yview)

        self.pharmacy_table["show"] = "headings"

        self.pharmacy_table.heading("refno", text="Reference No")
        self.pharmacy_table.heading("cmpName", text="Company Name")
        self.pharmacy_table.heading("type", text="Type Of Medicine")
        self.pharmacy_table.heading("tablename", text="Tablet Name")
        self.pharmacy_table.heading("lotno", text="Lot no")
        self.pharmacy_table.heading("issuedate", text="Issue Date")
        self.pharmacy_table.heading("expdate", text="Exp Date")
        self.pharmacy_table.heading("uses", text="uses")
        self.pharmacy_table.heading("sideeffect", text="Side Effect")
        self.pharmacy_table.heading("warning", text="Prec&Warning")
        self.pharmacy_table.heading("dosge", text="dosge")
        self.pharmacy_table.heading("price", text="Price")
        self.pharmacy_table.heading("product", text="Product Qt")
        self.pharmacy_table.pack(fill=BOTH, expand=1)

        self.pharmacy_table.column("refno", width=100)
        self.pharmacy_table.column("cmpName", width=100)
        self.pharmacy_table.column("type", width=100)
        self.pharmacy_table.column("tablename", width=100)
        self.pharmacy_table.column("lotno", width=100)
        self.pharmacy_table.column("issuedate", width=100)
        self.pharmacy_table.column("expdate", width=100)
        self.pharmacy_table.column("uses", width=100)
        self.pharmacy_table.column("sideeffect", width=100)
        self.pharmacy_table.column("warning", width=100)
        self.pharmacy_table.column("dosge", width=100)
        self.pharmacy_table.column("price", width=100)
        self.pharmacy_table.column("product", width=100)
        self.fetch_dataMed()
        self.fatch_data()
        self.pharmacy_table.bind("<ButtonRelease-1>", self.get_cursor)

        # # ==================ADD MEDICINE FUNCTIONALITY DECLARATION==================

    def AddMed(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Roshan@01", database="mydata")
        my_cursor = conn.cursor()
        print((
            self.refMed_var.get(),
            self.addmed_var.get()

        ))
        if not self.refMed_var.get()  or not self.addmed_var.get() :
            messagebox.showerror("Error", "All Fields are required")
            return
        my_cursor.execute("insert into pharma(Ref,MedName) values(%s,%s)", (
            self.refMed_var.get(),
            self.addmed_var.get()

        ))

        conn.commit()
        self.fetch_dataMed()
        self.Medget_cursor()
        conn.close()
        messagebox.showinfo("Success", "Medicine Added")

    def fetch_dataMed(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Roshan@01", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharma")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.medicine_table.delete(*self.medicine_table.get_children())
            for i in rows:
                self.medicine_table.insert("", END, values=i)
            conn.commit()
        conn.close()

        # # =====================Med GET CURSOR=================================

    def Medget_cursor(self, event=""):
        cursor_row = self.medicine_table.focus()
        content = self.medicine_table.item(cursor_row)
        row = content["values"]
        self.refMed_var.set(row[0])
        self.addmed_var.set(row[1])

    def UpdateMed(self):
        if self.refMed_var.get() == "" or self.addmed_var.get() == "":
            messagebox.showerror("Error", "All fields are Required")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Roshan@01", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("update pharma set MedName=%s where Ref=%s", (
                self.addmed_var.get(),
                self.refMed_var.get(),
            ))
            conn.commit()
            self.fetch_dataMed()
            conn.close()

            messagebox.showinfo("Success", "Medicine has been Updated")

    def DeleteMed(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Roshan@01", database="mydata")
        my_cursor = conn.cursor()

        sql = "delete from pharma where Ref=%s"
        val = (self.refMed_var.get(),)
        my_cursor.execute(sql, val)

        conn.commit()
        self.fetch_dataMed()
        conn.close()

    def ClearMed(self):
        self.refMed_var.set("")
        self.addmed_var.set("")

    # # =============================MAIN TABLE=====================================

    def add_data(self):
        if self.ref_var.get() == "" or self.lot_var.get() == "":
            messagebox.showerror("Error", "All Fields are required")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Roshan@01", database="mydata")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into pharmacy values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.ref_var.get(),
                self.cmpName_var.get(),
                self.typeMed_var.get(),
                self.medName_var.get(),
                self.lot_var.get(),
                self.issuedate_var.get(),
                self.expdate_var.get(),
                self.uses_var.get(),
                self.sideEffect_var.get(),
                self.warning_var.get(),
                self.dosage_var.get(),
                self.price_var.get(),
                self.product_var.get()
            ))
            conn.commit()
            self.fatch_data()
            conn.close()
            messagebox.showinfo("Success", "Data has been inserted")

    def fatch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Roshan@01", database="mydata")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from pharmacy")
        row = my_cursor.fetchall()
        if len(row) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in row:
                self.pharmacy_table.insert("", END, value=i)
            conn.commit()
        conn.close()

    def get_cursor(self, ev=""):
        cursor_row = self.pharmacy_table.focus()
        content = self.pharmacy_table.item(cursor_row)
        row = content["values"]

        self.ref_var.set(row[0]),
        self.cmpName_var.set(row[1]),
        self.typeMed_var.set(row[2]),
        self.medName_var.set(row[3]),
        self.lot_var.set(row[4]),
        self.issuedate_var.set(row[5]),
        self.expdate_var.set(row[6]),
        self.uses_var.set(row[7]),
        self.sideEffect_var.set(row[8]),
        self.warning_var.set(row[9]),
        self.dosage_var.set(row[10]),
        self.price_var.set(row[11]),
        self.product_var.set(row[12])

    def Update(self):
        if self.ref_var.get() == "" or self.lot_var.get() == "":
            messagebox.showerror("Error", "All fields are Required")
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="Roshan@01", database="mydata")
            my_cursor = conn.cursor()
            data = (self.cmpName_var.get(),
                    self.typeMed_var.get(),
                    self.medName_var.get(),
                    self.lot_var.get(),
                    self.issuedate_var.get(),
                    self.expdate_var.get(),
                    self.uses_var.get(),
                    self.sideEffect_var.get(),
                    self.warning_var.get(),
                    self.dosage_var.get(),
                    self.price_var.get(),
                    self.product_var.get(),
                    self.ref_var.get()
                    )

            my_cursor.execute("update pharmacy set cmpName=%s,Type=%s,medname=%s,lot=%s,issuedate=%s,expdate=%s,uses=%s,sideeffect=%s,\
                                warning=%s,dosge=%s,price=%s,product=%s where refno=%s", data)
            conn.commit()
            self.fatch_data()
            conn.close()

            messagebox.showinfo(
                "UPDATE", "Record has been updated successfully")

    def delete(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Roshan@01", database="mydata")
        my_cursor = conn.cursor()

        sql = "delete from pharmacy where refno=%s"
        val = (self.ref_var.get(),)
        my_cursor.execute(sql, val)

        conn.commit()
        self.fatch_data()
        conn.close()

        messagebox.showinfo("Delete", "Info deleted Successfully")

    def reset(self):
        # self.ref_var.set(""),
        self.cmpName_var.set(""),
        # self.typeMed_var.set(""),
        # self.medName_var.set(""),
        self.lot_var.set(""),
        self.issuedate_var.set(""),
        self.expdate_var.set(""),
        self.uses_var.set(""),
        self.sideEffect_var.set(""),
        self.warning_var.set(""),
        self.dosage_var.set(""),
        self.price_var.set(""),
        self.product_var.set("")

    def search_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="Roshan@01", database="mydata")
        my_cursor = conn.cursor()
        # my_cursor.execute("select * from pharmacy where refno=101")
        my_cursor.execute("select * from pharmacy where "+(self.search_var.get()) +" = "+ (self.serchTxt_var.get()))
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.pharmacy_table.delete(*self.pharmacy_table.get_children())
            for i in rows:
                self.pharmacy_table.insert("", END, value=i)
            conn.commit()
        conn.close()
    def ex(self):
        exit()

if __name__ == "__main__":
    root = Tk()
    obj = PharmacyManagementSystem(root)
    root.mainloop()
