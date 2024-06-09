from tkinter import *
def sayHelloWorld() :
    print("Hello World")

MainWindow = Tk()
Button1 = Button(MainWindow,text = "Click me1",width=20, command = sayHelloWorld()).grid(row = 0,column = 1)
Button2 = Button(MainWindow,text = "Click me2",command = sayHelloWorld()).grid(row = 1,column = 2)
lebel = Label(MainWindow,text= "Hello World",font= ("Helvetica",38),anchor= E,width= 20,fg= "red",bg= "blue").grid(row= 0,column= 1)
MainWindow.mainloop()