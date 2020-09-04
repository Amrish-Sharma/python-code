import tkinter as tk
import tkinter.ttk
import sqlite3 as lite
from sqlite3 import Error

master = tk.Tk()
master.geometry("440x210")
master.title("Employee Entry")


create_users_sql = "CREATE TABLE users (name TEXT, idnumber TEXT,department NUMBER,jobtitle TEXT)"




#Creating the GUI
tk.Label(master, 
         text="Name").grid(row=2)
         
tk.Label(master, 
         text="ID Number").grid(row=3)
tk.Label(master, 
         text="Department").grid(row=4)
tk.Label(master, 
         text="Job Title").grid(row=5)


e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)
e4 = tk.Entry(master)

e1.grid(row=2,column=2)
e2.grid(row=3, column=2)
e3.grid(row=4, column=2)
e4.grid(row=5, column=2)


def savedata():
#taking inputs in variable    
    name=str(e1.get())
    idnumber=int(e2.get())
    department=str(e3.get())
    jobtitle=str(e4.get())
    #creating new database
    try:
        conn = lite.connect("mydatabase.db")
        create_users_sql = "CREATE TABLE if not exists users (name TEXT, idnumber TEXT,department NUMBER,jobtitle TEXT)"
        conn.execute(create_users_sql)

        insert_users="INSERT INTO users VALUES (?,?,?,?);" 
        conn.execute(insert_users,(name, idnumber,department,jobtitle))
        conn.commit()
        print("user: {} inserted successfully".format(name))
    except:
        print("something went wrong")

def show_data():
    conn = lite.connect("mydatabase.db")
    cur=conn.cursor()
    show_users="select * from users"
    cur.execute(show_users)

    rows=cur.fetchall()

    for row in rows:
        print(row)
    

        


    

tk.Button(master, 
          text='Add To File',command=savedata).grid(row=6, 
                                    column=2, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='Next Data',command=show_data).grid(row=7, 
                                    column=2, 
                                    sticky=tk.W, 
                                    pady=4)
      


master.mainloop()