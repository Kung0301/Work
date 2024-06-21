from currency_converter import CurrencyConverter
from tkinter import *
c = CurrencyConverter()

def leftclickbuttonUSD(event) :
    usd = float(entry1.get())
    result1.configure(text=c.convert(usd,'THB','USD'))
def leftclickbuttonCNY(event) :
    usd = float(entry1.get())
    result1.configure(text=c.convert(usd,'THB','CNY'))
def leftclickbuttonJPY(event) :
    usd = float(entry1.get())
    result1.configure(text=c.convert(usd,'THB','JPY'))
def leftclickbuttonSGD(event) :
    usd = float(entry1.get())
    result1.configure(text=c.convert(usd,'THB','SGD'))
def leftclickbuttonGBP(event) :
    usd = float(entry1.get())
    result1.configure(text=c.convert(usd,'THB','GBP'))


mainWindow = Tk()
label1 = Label(mainWindow,text="โปรดใส่จำนวนเงิน (THB)")
label1.grid(row=0,column=0)
entry1 = Entry(mainWindow)
entry1.grid(row=1,column=0)
button1 = Button(mainWindow,text="USD")
button1.bind('<Button-1>',leftclickbuttonUSD)
button1.grid(row=0,column=1)
button2 = Button(mainWindow,text="CNY")
button2.bind('<Button-1>',leftclickbuttonCNY)
button2.grid(row=1,column=1)
button3 = Button(mainWindow,text="JPY")
button3.bind('<Button-1>',leftclickbuttonJPY)
button3.grid(row=2,column=1)
button4 = Button(mainWindow,text="SGD")
button4.bind('<Button-1>',leftclickbuttonSGD)
button4.grid(row=3,column=1)
button5 = Button(mainWindow,text="GBP")
button5.bind('<Button-1>',leftclickbuttonGBP)
button5.grid(row=4,column=1)
result1 = Label(mainWindow,text="")
result1.grid(row=2,column=0)
mainWindow.mainloop()

