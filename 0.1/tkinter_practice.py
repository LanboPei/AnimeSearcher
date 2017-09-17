from tkinter import *

def l1():
    print("Lanbo")

def l2(event):
    print(event.time, event.type)

def l3(event):
    print("moveover")

def button():
    b1 = Button(root, text="click1", command = l1, width = 24)
    b1.pack()
    b2 = Button(root, text="click2", width = 24)
    b2.bind("<Enter>", l2)
    b2.pack()

def entry():
    e = Entry(root, text = "input your name")
    e.pack()
    b = Button(root, text = "getMessage", command = get(e))

def get():
##    print(e.get())
    t['text'] = e.get()


root = Tk()

##button()
e = Entry(root, text = "input your name")
e.pack()
b = Button(root, text = "getMessage", command = get)
b.pack()

t = Label(root, text = "wait4info")
t.pack()


root.mainloop()
