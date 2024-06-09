from tkinter import *
def leftClickButton(event) :
    print("Left click")
def rightClickButton(event) :
    print("Double click")

main = Tk()
button = Button(main,text= "My button")
button.pack()
button.bind('<Button-1>',leftClickButton)
button.bind('<Double-1>',rightClickButton)
main.mainloop()