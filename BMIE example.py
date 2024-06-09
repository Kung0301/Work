from tkinter import *
import math
def leftClickButton(event) :
 h = float(textboxHeight.get())
 w = float(textboxWeight.get())
 BMI = w/((h/100)**2)
 if BMI < 18.5 :
  labelResult.configure(text= "ตั่ากว่าเกณฑ์")
 elif BMI < 22.9 :
  labelResult.configure(text= "สมส่วน")
 elif BMI < 24.9 :
  labelResult.configure(text= "นํ้าหนักเกิน")
 elif BMI < 29.9 :
  labelResult.configure(text= "อ้วนระดับ 1")
 else :
  labelResult.configure(text= "อ้วนระดับ 2")


mainwindow = Tk()
labelHeight = Label(mainwindow,text= "Height cm.)")
labelHeight.grid(row= 0,column= 0)
textboxHeight = Entry(mainwindow)
textboxHeight.grid(row= 0,column= 1)
labelWeight = Label(mainwindow,text= "Weight (kg.)")
labelWeight.grid(row= 1,column= 0)
textboxWeight = Entry(mainwindow)
textboxWeight.grid(row= 1,column= 1)
calculateButton = Button(mainwindow,text= "Calculate")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row= 2,column= 0)
labelResult = Label(mainwindow,text= "Result")
labelResult.grid(row= 2,column= 1)
mainwindow.mainloop()