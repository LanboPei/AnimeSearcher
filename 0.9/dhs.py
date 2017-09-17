from tkinter import *
from searcher import *
import webbrowser

'''
urlopen with Chinese input
https://www.zhihu.com/question/22899135
'''

AnimeName = ''
URL = ''
Rating = ''
RText = "Rating in Bangumi:    "
    

def goSearch():
    name = e.get()
    name = parseZH(name)
    
    global Rating
    global URL
    Rating, URL = search(name)   
    t1['text'] = RText[:-3] + Rating

def parseZH(zhString):
    return urllib.parse.quote(zhString)

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
