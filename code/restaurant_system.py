

from tkinter import *

import time
import random


def clicked():

    #global v0,v6,v7,v8,v9

    r = random.randrange(100000, 200000)
    v0.set(r)

    # ------------list of prices--------------
    #chicken_p = 5
    #burger_p = 12
    #filet_o_meal = 15
    #fries_p = 3
    #drinks_p = 2
    #tax = 0.2 %

    b = 12*int(v1.get())
    c = 5*int(v2.get())
    fo = 15*int(v3.get())
    fr = 3*int(v4.get())
    dr = 2*int(v5.get())

    subtotal = b+c+fo+fr+dr
    m = str("$") + str(subtotal)
    v6.set(m)

    tax = float(subtotal*0.2)
    tx = str("$") + str(float("%.2f" % tax))
    v7.set(tx)

    service_c = float(subtotal/99)
    sc = str("$") + str(float("%.2f" % service_c))
    v8.set(sc)

    total = str("$") + str(float("%.2f" % (subtotal+service_c+tax)))

    v9.set(total)


def reset():

    v0.set("")
    v1.set("")
    v2.set("")
    v3.set("")
    v4.set("")
    v5.set("")
    v6.set("")
    v7.set("")
    v8.set("")
    v9.set("")


root = Tk()
root.title("Restaurant Management System")
root.geometry("1200x600")

tframe = Frame(root,bg = 'powder blue')
tframe.pack(side = TOP)

bframe = Frame(root)
bframe.pack(side = BOTTOM)


frame1 = Frame(root)
frame1.pack(side = LEFT)

frame2 = Frame(root)
frame2.pack(side = RIGHT)

t = time.asctime(time.localtime(time.time()))


lbl1 = Label(tframe,text = "Restaurant Management System",font = ("arial",18,"bold"),fg = "steel blue")

lbl1.grid(row = 5,column = 0,sticky = E)

lbl2 = Label(tframe,text = t,font = ("arial",15,"bold"),fg = "steel blue")
lbl2.grid(row = 0,column = 0)

v0 = StringVar()

lb0 = Label(frame1,text = "Reference Number",font = ("arial",13,"bold"))
lb0.grid(row = 0,column = 0)
entry0 = Entry(frame1,insertwidth = 8,textvariable = v0,bg = "powder blue",bd = 13,font = ("arial",13,"bold"))

entry0.grid(row = 0,column =2)

v1 = StringVar()

lb1 = Label(frame1,text = "Burger Meal",font = ("arial",13,"bold"))
lb1.grid(row = 1,column = 0,sticky = E)
entry1 = Entry(frame1,textvariable = v1,insertwidth = 8,bg = "powder blue",bd = 13,font = ("arial",13,"bold"))
entry1.grid(row = 1,column =2)


v2 = StringVar()

lb2 = Label(frame1,text = "Chicken Meal",font = ("arial",13,"bold"))
lb2.grid(row = 2,column = 0,sticky = E)
entry2 = Entry(frame1,textvariable = v2,insertwidth = 8,bg = "powder blue",bd = 13,font = ("arial",13,"bold"))
entry2.grid(row = 2,column =2)

v3 = StringVar()

lb3 = Label(frame1,text = "Filet-O-Meal",font = ("arial",13,"bold"))
lb3.grid(row = 3,column = 0,sticky = E)
entry3 = Entry(frame1,textvariable = v3,insertwidth = 8,bg = "powder blue",bd = 13,font = ("arial",13,"bold"))
entry3.grid(row = 3,column =2)

v4 = StringVar()

lb4 = Label(frame1,text = "Fries Pack",font = ("arial",13,"bold"))
lb4.grid(row = 4,column = 0,sticky = E)
entry4 = Entry(frame1,textvariable = v4,insertwidth = 8,bg = "powder blue",bd = 13,font = ("arial",13,"bold"))
entry4.grid(row = 4,column =2)

v5 = StringVar()

lb5 = Label(frame2,text = "Drinks",font = ("arial",13,"bold"))
lb5.grid(row = 1,column = 0,sticky = E)
entry5 = Entry(frame2,textvariable = v5,insertwidth = 8,bg = "powder blue",bd = 13,font = ("arial",13,"bold"))
entry5.grid(row = 1,column =2)

v6 = StringVar()

lb6 = Label(frame2,text = "Sub Total(Cost of Meal)",font = ("arial",13,"bold"))
lb6.grid(row = 2,column = 0,sticky = E)
entry6 = Entry(frame2,textvariable = v6,insertwidth = 8,bg = "powder blue",bd = 13,font = ("arial",13,"bold"))
entry6.grid(row = 2,column =2)

v7 = StringVar()

lb7 = Label(frame2,text = "State Tax",font = ("arial",13,"bold"))
lb7.grid(row = 3,column = 0,sticky = E)
entry7 = Entry(frame2,textvariable = v7,insertwidth = 8,bg = "powder blue",bd = 13,font = ("arial",13,"bold"))
entry7.grid(row = 3,column =2)

v8 = StringVar()

lb8 = Label(frame2,text = "Service Charge",font = ("arial",13,"bold"))
lb8.grid(row = 4,column = 0,sticky = E)
entry8 = Entry(frame2,textvariable = v8,insertwidth = 8,bg = "powder blue",bd = 13,font = ("arial",13,"bold"))
entry8.grid(row = 4,column =2)

v9 = StringVar()


btn9 = Button(bframe,text = "Click here to calculate total",font = ("arial",15,"bold"),command = clicked)
btn9.grid(row = 0,column = 0)

btnr = Button(bframe,text = "Reset",font = ("arial",15,"bold"),width = 9,command = reset)
btnr.grid(row = 0,column = 5)

lb9 = Label(bframe,text = "Total Cost",font = ("arial",20,"bold"))
lb9.grid(row = 9,column = 0)
entry9 = Entry(bframe,textvariable = v9,insertwidth = 8,bg = "powder blue",bd = 13,font = ("arial",20,"bold"))
entry9.grid(row = 9,column =2)

btnq = Button(bframe,text = "Quit",font = ("arial",15,"bold"),width = 9,command = root.destroy)
btnq.grid(row = 0,column = 6)


root.mainloop()