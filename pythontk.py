#importing Tkinter module for the GUI
import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os

class GUI():
#a constructor which intializes all the window whenever we make a call to the GUI class
    def __init__(self):
        #responsible for making window
        #self.root is provide so that it can be made global and referenced in any function
        self.root=Tk()
        #using .title: provides a title to the window
        self.root.title('Employee Wages')
        #For storing values from the GUI window - need to define variables as StringVar()
        self.first_name=StringVar()
        self.last_name=StringVar()
        self.num_hrs_worked=StringVar()
        self.hourly_rate=StringVar()

        #Labels are responsible for showing text in the window
        #.grid() divides the whole window into grids
        self.emp_firstnamelabel = Label(self.root, text='First Name : ').grid(row=0, sticky=W, padx=4)
        
        #defining textvariable=self.f_name makes its a reference to the entry(Input)
        self.emp_firstname = Entry(self.root, textvariable=self.first_name)
        
        self.emp_firstname.grid(row=0, column=1, sticky=E, padx=4)

        self.emp_lastnamelabel = Label(self.root, text='Last Name : ').grid(row=1, sticky=W, padx=4)
        self.emp_lastname = Entry(self.root, textvariable=self.last_name)
        
        # all entry text needs to be clear by the button clear so we are using it seperatly.
        self.emp_lastname.grid(row=1, column=1, sticky=E, padx=4)

        self.emp_hourslabel = Label(self.root, text='Num of hours worked : ').grid(row=2, sticky=W, padx=4)
        self.emp_hours = Entry(self.root, textvariable=self.num_hrs_worked)
        self.emp_hours.grid(row=2, column=1, sticky=E, padx=4)

        self.emp_hourwageratelabel = Label(self.root, text='Hourly pay rate : ').grid(row=3, sticky=W, padx=4)
        self.emp_hourwagerate = Entry(self.root, textvariable=self.hourly_rate)
        self.emp_hourwagerate.grid(row=3, column=1, sticky=E, padx=4)

        #after the button grosspay is clicked we are going to call the function grosspay and pass the value
        #as above defined variable are reference so we are .get() to get their values
        self.grosspaybutton = Button(self.root, text='Gross Pay', fg='white', bg='green',
        command=lambda: self.grosspay(self.num_hrs_worked.get(),self.hourly_rate.get())).grid(row=5, column=1)

        self.saveDatabutton = Button(self.root, text='Save to File', fg='white', bg='blue',
        command=lambda: self.saveData()).grid(row=6, column=1)

        self.closebutton = Button(self.root, text='Close', fg='white', bg='red',
        command=lambda: self.close()).grid(row=6, column=0)

        self.clearbutton = Button(self.root, text='Clear', fg='white', bg='red',
        command=lambda: self.clear()).grid(row=6, column=2)

        #holds the window on the screen
        self.root.mainloop()


    #function called when the gross pay button is clicked by the user
    def grosspay(self,num_hrs_worked,hourly_rate):
        #change stringVar into int for calculations
        num_hrs_worked=int(num_hrs_worked)
        hourly_rate=int(hourly_rate)
        self.total_income=0
        if(num_hrs_worked>40):
            self.total_income=(hourly_rate*40)+((num_hrs_worked-40)*(hourly_rate*1.5))
        else:
            self.total_income=hourly_rate*num_hrs_worked

        #define a label which will be showed for the gross pay when user clicks the button
        self.emp_grosslabel = Label(self.root, text="Gross Pay : ")
        self.emp_grosslabel.grid(row=4, sticky=W, padx=4)
        self.emp_grosslabel = Label(self.root, text=self.total_income)
        self.emp_grosslabel.grid(row=4, column=1, sticky=W, padx=4)


    #function called by clicking on save data to file button
    def saveData(self):
        #checks for existing file - saves to file if exists, creates and saves data to file if it does not exist
        self.f = open("employeeWages.txt", "a")
        #write the data to the file on a single line
        self.f.write("Name: %s %s Number of Hours Worked: %s Wage per Hours: %s Total Income: %s\n"
        %(self.first_name.get(),self.last_name.get(),self.num_hrs_worked.get(),self.hourly_rate.get(),self.total_income))

    #function called by clicking on the 'Close' to close the window.
    def close(self):
        self.root.destroy()


#calling function to clear the data once 'clear' button is pressed
    def clear(self):
        self.emp_firstname.delete(0,END)
        self.emp_lastname.delete(0,END)
        self.emp_hours.delete(0,END)
        self.emp_hourwagerate.delete(0,END)
        self.emp_grosslabel.destroy()
        self.emp_grosslabel.destroy()
  

# making a simple call or you can say object making
GUI()