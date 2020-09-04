import tkinter as tk
import tkinter.ttk


master = tk.Tk()
master.geometry("440x210")
master.title("JOB FAIR ATTENDANCE PORTAL")
tk.Label(master,text="JOB FAIR ATTENDANCE",fg="red").grid(row=0,column=2)

def lookup():
    try:
        month=e0.get()
        #global senior,junior,sophomore,freshman
        with open('JobFair.txt','r') as read_obj:
            for line in read_obj:
                words=line.strip().split(",")
                #print(words[1])
                
                if month in words[0]:
                    if 'Senior' in words[1]:
                        senior=int(words[2])
                    elif 'Junior' in words[1]:
                        junior=int(words[2])
                    elif 'Sophomore' in words[1]:
                        sophomore=int(words[2])
                    elif 'Freshman' in words[1]:
                        freshman=int(words[2])
        count=senior+junior+sophomore+freshman
        print(freshman,sophomore,junior,senior,count)

        e1.delete(0, tk.END)
        e2.delete(0, tk.END)
        e3.delete(0, tk.END)
        e4.delete(0, tk.END)
        e5.delete(0, tk.END)


        e1.insert(0,freshman)
        e2.insert(0,sophomore)
        e3.insert(0,junior)
        e4.insert(0,senior)
        e5.insert(0,count)
    except:
        print("Something went wrong")



#Creating the GUI
tk.Label(master, 
         text="MONTH").grid(row=2)
         
tk.Label(master, 
         text="Enter a month then click LOOKUP\n\
         to search the data",font=("Helvetica", 7),bg="white").grid(row=3)
tk.Label(master, 
         text="Freshman").grid(row=5,column=2)
tk.Label(master, 
         text="Sophomore").grid(row=6,column=2)
tk.Label(master, 
         text="Junior").grid(row=7,column=2)
tk.Label(master, 
         text="Senior").grid(row=8,column=2)

#tk.ttk.Separator(master).grid(row=9, column=0, columnspan=3, sticky='ns')

tk.Label(master, 
         text="Total").grid(row=10,column=2)

e0=tk.Entry(master)
e1 = tk.Entry(master,bg="grey")
e2 = tk.Entry(master,bg="grey")
e3 = tk.Entry(master,bg="grey")
e4 = tk.Entry(master,bg="grey")
e5=tk.Entry(master)



e0.grid(row=2,column=2)
e1.grid(row=5, column=3)
e2.grid(row=6, column=3)
e3.grid(row=7, column=3)
e4.grid(row=8, column=3)
e5.grid(row=10, column=3)


    

tk.Button(master, 
          text='LOOKUP',command=lookup).grid(row=2, 
                                    column=3, 
                                    sticky=tk.W, 
                                    pady=4)
tk.Button(master, 
          text='QUIT',command=master.destroy).grid(row=3, 
                                    column=3, 
                                    sticky=tk.W, 
                                    pady=4)
      


master.mainloop()