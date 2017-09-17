from tkinter import *
from searcher import *
import webbrowser

##def l1():
##    print("Lanbo")
##
##def l2(event):
##    print(event.time, event.type)
##
##def l3(event):
##    print("moveover")
##
##def button():
##    b1 = Button(root, text="click1", command = l1, width = 24)
##    b1.pack()
##    b2 = Button(root, text="click2", width = 24)
##    b2.bind("<Enter>", l2)
##    b2.pack()
##
##def entry():
##    e = Entry(root, text = "input your name")
##    e.pack()
##    b = Button(root, text = "getMessage", command = get(e))
##
##def get():
##    t['text'] = e.get()
##
##
##root = Tk()
##
##e = Entry(root, text = "input your name")
##e.pack()
##b = Button(root, text = "getMessage", command = get)
##b.pack()
##
##t = Label(root, text = "wait4info")
##t.pack()
##
##
##root.mainloop()
AnimeName = ''
URL = ''
Rating = ''
RText = "Rating in Bangumi:    "
    

def goSearch():
    name = e.get()
    global Rating
    global URL
    Rating, URL = search(name)   
    t1['text'] = RText[:-3] + Rating

def goBangumi():
    webbrowser.open(URL)
    

if __name__ == "__main__":
    root = Tk()



    e = Entry(root)
    e.pack()

    b1 = Button(root, text = "Search", command = goSearch)
    b1.pack()

    t1 = Label(root, text = RText)
    t1.pack()

    b2 = Button(root, text = "Go Bangumi", command = goBangumi)
    b2.pack()

    root.mainloop()
