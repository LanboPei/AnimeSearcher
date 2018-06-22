from tkinter import *  #Library: Python's de-facto standard GUI, including Tk
import webbrowser      #Module
from searcher import * #Local: search engine

'''
urlopen with Chinese input
https://www.zhihu.com/question/22899135

Using class implementation to easily share variables (attributes).
'''

WIDTH = 400 #Width of main window
HEIGHT = 200 #Height of main window
XOFFSET = 0 #X dimension offset of main window, if needed
YOFFSET = 0 #Y dimension offset of main window, if needed

ENTER_RETURN = '<Key-Return>'

PROMPT_W = 350 #Width of pop-up prompt
PROMPT_H = 50 #Height of pop-up prompt
PROMPT_EMPTY = "Please enter the name of the anime you want to search for."
PROMPT_NO_RESULT = "No result found."
#Text for empty input

BGMText = "Rating on Bangumi:   " #Text prefix for rating display from Bangumi


class DHS:
    '''
    This class serves as the base of the anime searching. It is responsible for
    forming the UI and being an I/O interface bewteen data and the engine.
    '''

    def __init__(self, width, height, xoffset=0, yoffset=0):
        '''
        Create a new DHSearcher.
        
        @param width: The width of the application window.
        @param height: The height of the application windwo.
        @param xoffset: The X dimension offset for the window. Default 0 means
                        the middle of the x-axis of the screen, + means right
                        side and - means left side.
        @param yoffset: The Y dimension offset for the window. Default 0 means
                        the middle of the y-axis of the screen, + means up side
                        and - means down side.
        
        '''
        
        self.root = Tk()
        self.w = width
        self.h = height
        self.xo = xoffset
        self.yo = yoffset
        self.url = ''     
        self.text = {}
        self.entry = {}


    def prePosition(self):
        '''
        Place the main window at the desired position. Get the x-y coordinate
        first.
        '''

        x, y = self.getXY(self.w, self.h)
        self.root.geometry("{}x{}+{}+{}".format(WIDTH, HEIGHT, x, y))
            #Tk.geometry() takes a formative string as shown above. This string
            #contains 4 ints, which are width and height of the application
            #window, and x, y coordinates of top left corner of the window on
            #the screen. It then sets the right position of the window according
            #to these input.


    def getXY(self, winWidth, winHeight):
        '''
        Return calculated x, y coordinates of the top left corner of the window,
        given consideration on offsets as well.

        @param winWidth: Width of the window to be positioned.
        @param winHeight: Height of the window to be positioned.
        '''

        root = self.root
        x = int(abs((root.winfo_screenwidth() - winWidth) / 2)) + self.xo
        y = int(abs((root.winfo_screenheight() - winHeight) / 2)) + self.yo
            #Use Tk.winfo methods to get width and height of the scree. Along
            #with window's width and height, as well as the offsets, calculate
            #final x, y.
        return x, y


    def newEntry(self, name, binding=None):
        '''
        Return an Entry object. Create a new Entry in the window which serves as
        input box, then save this Entry to the dict of entries of this DHS.
        
        @param name: Naming label for this specific entry.
        @param binding: Key-Function tuple to be binded to this Entry.
                        Key is a string representation of a specific key, and
                        Function is the function (usually lambda) to be binded.
        '''
        e = Entry(self.root) #Entry serves as an input filed in tkinter.
        self.entry[name] = e
        if binding:
            e.bind(binding[0], binding[1])
        e.pack() #Finish packaging and make this available. Same for other
                 #tkinter object instances.
        return e


    def newButton(self, name, txt, cmd, binding=None):
        '''
        Return a Button object. Create a new Button in the window.
        
        @param name: Naming label for this specific button.
        @param txt: Text shown on this button.
        @param cmd: Function run when clicking this button.
        @param binding: Key-Function tuple to be binded to this Entry.
                        Key is a string representation of a specific key, and
                        Function is the function (usually lambda) to be binded.
        '''

        b = Button(self.root, text=txt, command=cmd)
        if binding:
            b.bind(binding[0], binding[1])
        b.pack()
        return b


    def newText(self, name, txt):
        '''
        Return a Label object. Create a new Label in the window which serves as
        text display.
        
        @param name: Naming label for this specific button.
        @param txt: Text shown on this button.
        @param cmd: Function run when clicking this button.
        '''
        
        t = Label(self.root, text=txt)
        t.pack()
        self.text[name] = t
        return t


    def goSearch(self):
        '''
        Call the search engine to perform the search. Get the input anime name
        first. Examine if it is empty. Pass the input to the engine, get and set
        the returned rating and page url of the searched anime on Bangumi.
        '''
        
        name = self.entry["search"].get()
        if name == '':
            self.prompt(name) #Prompt if the input is empty
        else:
            #namewords = name.split() #
            #for i in range(len(namewords)):
            #    namewords[i] = parseZH(namewords[i])
            rating, self.url = search(name)
            if not rating:
                self.prompt(rating)
            else:
                t = self.text["rating"]
                t['text'] = BGMText + rating


    def goBangumi(self):
        webbrowser.open(self.url)


    def prompt(self, txt):
        '''
        Pop up a prompt to inform the user.

        @param txt: The text to be displayed.
        '''
        
        top = Toplevel(self.root)

        if txt == '':
            txt = PROMPT_EMPTY #empty prompt here
        elif not txt:
            txt = PROMPT_NO_RESULT
        
        msg = Message(top, text=txt, width=600)
        msg.pack()
        w = PROMPT_W
        h = PROMPT_H
        x, y = self.getXY(w, h)
        top.geometry("{}x{}+{}+{}".format(w, h, x, y))

        b = Button(top, text='OK', command=top.destroy)
        b.bind(ENTER_RETURN, lambda event:top.destroy())
        b.pack()
        b.focus()


    def start(self):
        self.root.mainloop()
    

if __name__ == "__main__":
    dhs = DHS(WIDTH, HEIGHT)
    dhs.prePosition()

    e = dhs.newEntry("search", (ENTER_RETURN, lambda event:dhs.goSearch()))
        #Keyboard binding this Entry and the return/enter key, so that start
        #searching right after name input and return/enter key pressing. Use
        #lambda exp to avoid defing a trivial function.
    e.focus() #get default focus

    b1 = dhs.newButton("search", "Search", dhs.goSearch)

    t1 = dhs.newText("rating", BGMText)

    b2 = dhs.newButton("goBGM", "Go Bangumi", dhs.goBangumi,
                       (ENTER_RETURN, lambda event:dhs.goBangumi()))

    dhs.start()
