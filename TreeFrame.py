from tkinter import *
from tkinter.ttk import *
from Rectangle import Rectangle


class TreeFrame(Frame):
    def __init__(self, master=None, home_frame=None, tree_size=0, width=0, height=0):
        super().__init__(master, height=height, width=width)
        self.master = master
        self.tree_size = tree_size
        self.height = height
        self.width = width
        self.centerx = self.width / 2
        self.centery = self.height / 2
        self.treeContent = []
        self.frame = Frame(self.master)
        self.canvas = Canvas(self.frame, bg="#d0d0d0", height=self.height - 100,
                             width=self.width - 15)
        self.errlbl = Label(self.frame, text='')
        self.homeFrame = home_frame

    def add(self, value=None):
        size = len(self.treeContent)
        if size == self.tree_size:
            print('tree is full')
            self.errlbl.config(text='tree is full', foreground='red')
            return
        newElement = Rectangle(self.canvas)
        newElement.draw(self.centerx - 150, self.centery+100, 50, 50, value, 'green')
        newElement.move(self.master, self.centerx , self.centery + (50*self.tree_size) - (50 * (self.tree_size - 2 + len(self.treeContent))))
        # self.shift_elements(newElement)
        self.treeContent.append(newElement)

    def pop(self):
        size = len(self.treeContent)
        if size == 0:
            print('tree is empty')
            self.errlbl.config(text='tree is empty', foreground='red')
            return
        lastElement = self.treeContent.pop()
        lastElement.move(self.master, self.centerx+150, self.centery +100)

    def initialize(self):
        # display frame components
        frameLbl = Label(self.frame, text='Stack display frame')
        frameLbl.pack(anchor='center')

        self.canvas.pack(fill='both', expand=True)

        stackBody = Rectangle(self.canvas)
        stackBody.draw(self.centerx, self.centery-50,  50, self.tree_size * 50, None, 'yellow')

        inputFrame = Frame(self.frame)
        valueEntry = Entry(inputFrame)
        valueEntry.pack(side=LEFT)
        pushBtn = Button(inputFrame, text='Push', command=lambda: [self.add(valueEntry.get())])
        pushBtn.pack(side=LEFT)
        popBtn = Button(inputFrame, text='Pop', command=lambda: [self.pop()])
        popBtn.pack(side=LEFT)
        self.errlbl.pack(side=LEFT)
        inputFrame.pack()

        backBtn = Button(self.frame, text='Back', command=lambda: [self.hide(), self.clean_up()])
        backBtn.pack(side=BOTTOM, anchor='center')

    def clean_up(self):
        self.errlbl.config(text='')
        self.canvas.delete('all')
        for widget in self.frame.winfo_children():
            widget.pack_forget()

    def pack(self, fill, expand):
        self.frame.pack(fill=fill, expand=expand)

    def hide(self):
        self.frame.pack_forget()
        self.homeFrame.pack(fill="both", expand=True)
