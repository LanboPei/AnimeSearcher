from tkinter import *
from searcher import *
import webbrowser

'''
urlopen with Chinese input
https://www.zhihu.com/question/22899135

Using class implementation to easily share variables (attributes).
'''

WIDTH = 400
HEIGHT = 200
PROMPT_W = 350
PROMPT_H = 50

PROMPT_EMPTY = "Please enter the name of the anime you want to search for."

BGMText = "Rating in Bangumi:    "


class DHS:

    def __init__(self):
        #self.anime = ''
        self.url = ''
        #self.rateing = 0.0 #change "rating" from str to float
        #self.w = WIDTH
        #self.h = HEIGHT
        root = Tk()
        self.root = root
        self.sw = root.winfo_screenwidth()
        self.sh = root.winfo_screenheight()        
        self.text = {}
        self.button = {}
        self.entry = {}

    def prePosition(self):
        root = self.root
        x, y = calCenXY(self.sw, self.sh, WIDTH, HEIGHT)
        root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x, y))

    def newEntry(self, name):
        e = Entry(self.root)
        self.entry[name] = e
        return e

    def newButton(self, name, txt, cmd):
        b = Button(self.root, text=txt, command=cmd)
        self.button[name] = b
        return b

    def newText(self, name, txt):
        t = Label(self.root, text=txt)
        self.text[name] = t
        return t

    def goSearch(self):
        name = self.entry["search"].get()
        if name == '':
            self.prompt(name)
        else:
            name = parseZH(name)
            rating, self.url = search(name)
            t = self.text["rating"]
            t['text'] = BGMText[:-3] + rating



    def goBangumi(self):
        webbrowser.open(self.url)

##    def enterSearch(self, event):  #key-binding receive an "event" parameter
##        self.goSearch()
##
##    def enterBangumi(self, event):
##        self.goBangumi()

    def prompt(self, refer):
        top = Toplevel(self.root)

        t = ''
        if refer == '':
            t = PROMPT_EMPTY

        #top.geometry("400x100")
        
        msg = Message(top, text=t, width=600)
        msg.pack()
        w = PROMPT_W
        h = PROMPT_H
        x, y = calCenXY(self.sw, self.sh, w, h)
        top.geometry("{}x{}+{}+{}".format(w, h, x, y))

        b = Button(top, text='OK', command=top.destroy)
        b.bind('<Key-Return>', lambda event:top.destroy())
        b.pack()
        b.focus()

    #def promptInit(self, txt):

    #def enterDestroy(self, widget)

        

    def start(self):
        self.root.mainloop()

def parseZH(zhString):
    return urllib.parse.quote(zhString)

def calCenXY(screenWidth, screenHeight, windowWidth, windowHeight,
             xoffset=0, yoffset=0):
    sw = screenWidth
    sh = screenHeight
    w = windowWidth
    h = windowHeight
    x = int(abs((sw - w) / 2)) + xoffset
    y = int(abs((sh -h) / 2)) + yoffset
    return x, y

#def pprint(event):
#    print("teseste\n")
    

if __name__ == "__main__":
    dhs = DHS()

    dhs.prePosition() #position the window

    e = dhs.newEntry("search")
    e.bind('<Key-Return>', lambda event:dhs.goSearch()) #keyboard binding
                                                        #using lambda exp to
                                                        #avoid def trivial func
    e.pack()
    e.focus() #get default focus

    b1 = dhs.newButton("search", "Search", dhs.goSearch)
    b1.pack()

    t1 = dhs.newText("rating", BGMText)
    t1.pack()

    b2 = dhs.newButton("goBGM", "Go Bangumi", dhs.goBangumi)
    b2.bind('<Key-Return>', lambda event:dhs.goBangumi())
    b2.pack()

    dhs.start()
