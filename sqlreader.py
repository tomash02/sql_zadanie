from tkinter import *
import sqlite3

con = sqlite3.connect(':memory:')
cur = con.cursor()
sql_file = open('zaladunek_bazy_sales.sql')
sql_as_string = sql_file.read()
cur.executescript(sql_as_string)


class Checkbar(Frame):
    def __init__(self, parent=None, picks=[], side=LEFT, anchor=W):
        Frame.__init__(self, parent)
        self.vars = []
        for pick in picks:
            var = IntVar()
            chk = Checkbutton(self, text=pick, variable=var)
            chk.pack(side=side, anchor=anchor, expand=YES)
            self.vars.append(var)

    def state(self):
        return map((lambda var: var.get()), self.vars)


def jsj():
    columns = []
    boxes = list(options.state())
    for i in range(len(boxes)):
        if boxes[i] == 1:
            columns.append(i)

    name = name_str.get()
    mylist = Listbox(root, yscrollcommand=scrollbar.set)
    for row in cur.execute(f"SELECT * FROM sales_data WHERE Customer_Name LIKE '{name}'"):
        record = []
        for i in columns:
            record.append(row[i+1])
        mylist.insert(END, record)
    mylist.pack(expand=1, fill=BOTH)
    scrollbar.config(command=mylist.yview)


root = Tk()
root.geometry('1920x1080')
options = Checkbar(root, ["Order_ID",
                          "Order_Date",
                          "Ship_Date",
                          "Ship_Mode",
                          "Customer_ID",
                          "Customer_Name",
                          "Segment",
                          "Country",
                          "City",
                          "State",
                          "Region",
                          "Postal_Code",
                          "Product_ID",
                          "Category",
                          "Sub_Category",
                          "Product_Name",
                          "Sales",
                          "Quantity",
                          "Discount",
                          "Profit"])
options.pack(side=TOP, fill=X)
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)
name_str = StringVar()
name_label = Label(root, text="Podaj Imię", font=("bold", 14), padx=10)
name_label.pack()
name_entry = Entry(root, textvariable=name_str)
name_entry.pack()
weather_btn = Button(root, text="Szukaj", width=12, command=jsj, bg='grey')
weather_btn.pack()
mainloop()
