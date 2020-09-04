from tkinter import *
from tkinter import filedialog
import os
import Module

sale = Module.SalesReceipt()
global TransactionFile

def AddItem():
    sale.itemName = txtItemName.get()
    sale.itemPrice = float(txtItemPrice.get())
    sale.itemQty = int(txtItemQuantity.get())
    txtExtended.insert(END, format(sale.AddItem()))
    return

def OpenFile():
    SalesReceipt.filename='filename'
  
    saveFile = SalesReciept.filename + '.txt'
    
    TransactionFile = open(saveFile, 'w')

def Total():
    txtSaleTotal.delete(0, END)
    txtSaleTotal.insert(END, format(sale.SaleTotal()))
    txtTax.insert(END, format(sale.SalesTax()))
    txtTotal.delete(0, END)
    txtTotal.insert(END, format(sale.FinalSaleAmt()))
    for line in sale.SalesDetail():
        TransactionFile.write(line + '\n')

def ClearData():
    txtItemName.delete(0, END)
    txtItemPrice.delete(0, END)
    txtItemQuantity.delete(0, END)
    txtExtended.delete(0, END)
    txtTax.delete(0, END)
    txtItemName.focus()

def ExitProg():
    TransactionFile.close()
    SalesReceipt.destroy()
    return

SalesReceipt = Tk()
SalesReceipt.title('Transaction Receipt')
SalesReceipt.geometry('600x600')

lblItemName = Label(SalesReceipt, text = 'Item Descripton:')
txtItemName = Entry(SalesReceipt)
lblItemName.grid(row=0, column=0, sticky=E)
txtItemName.grid(row=0, column=1)

lblItemPrice = Label(SalesReceipt, text = 'Item Price:')
txtItemPrice = Entry(SalesReceipt)
lblItemPrice.grid(row=1, column=0, sticky=E)
txtItemPrice.grid(row=1, column=1)

lblItemQuantity = Label(SalesReceipt, text = 'Item Quantity:')
txtItemQuantity = Entry(SalesReceipt)
lblItemQuantity.grid(row=2, column=0, sticky=E)
txtItemQuantity.grid(row=2, column=1)

lblExtended = Label(SalesReceipt, text = 'Extended Price:')
txtExtended = Entry(SalesReceipt)
lblExtended.grid(row=3, column=0, sticky=E)
txtExtended.grid(row=3, column=1)

lblSaleTotal = Label(SalesReceipt, text = 'Sale Total:')
txtSaleTotal = Entry(SalesReceipt)
lblSaleTotal.grid(row=4, column=0, sticky=E)
txtSaleTotal.grid(row=4, column=1)

lblTax = Label(SalesReceipt, text = 'Sales Tax:')
txtTax = Entry(SalesReceipt)
lblTax.grid(row=5, column=0, sticky=E)
txtTax.grid(row=5, column=1)

lblTotal = Label(SalesReceipt, text = 'Grand Total:')
txtTotal = Entry(SalesReceipt)
lblTotal.grid(row=6, column=0, sticky=E)
txtTotal.grid(row=6, column=1)

buttonAddItem = Button(SalesReceipt, text = 'Add New Item')
buttonAddItem.grid(row=3, column=2, sticky=W)

buttonSaveItem = Button(SalesReceipt, text = 'Save to File')
buttonSaveItem.grid(row=3, column=3, sticky=W)

buttonGetTotal = Button(SalesReceipt, text = 'Total')
buttonGetTotal.grid(row=6, column=2, sticky=W)

buttonClearItem = Button(SalesReceipt, text = 'Clear')
buttonClearItem.grid(row=7, column=1, sticky=W)

buttonExit = Button(SalesReceipt, text = 'Exit')
buttonExit.grid(row=8, column=1, sticky=W)

SalesReceipt.mainloop()

