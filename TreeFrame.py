from tkinter import *
from tkinter.ttk import *

from Node import Node
from Rectangle import Rectangle


class TreeFrame(Frame):
    def __init__(self, master=None, home_frame=None, tree_size=0, width=0, height=0):
        super().__init__(master, height=height, width=width)
        self.root = Node(self.master)
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
        if size < 1:
            self.root.draw(self.centerx, self.centery - 50, 15, value, 'red')
            self.treeContent.append(self.root)
            return
        else:
            newElement = Node(self.canvas)
            newElement.draw(self.centerx - 150, self.centery + 100, 15, value, 'green')
            # newElement.move(self.master, self.centerx , self.centery + (50*self.tree_size) - (50 * (self.tree_size - 2 + len(self.treeContent))))
            # self.shift_elements(newElement)
            self.treeContent.append(newElement)

    def shift_elements(self, index, flag):
        size = len(self.treeContent)
        if size >= 1:
            if flag:
                for i in range(abs(index), size):
                    self.treeContent[i].move(self.master, self.centerx - 100 + (50 * i), self.centery - 100)
            else:
                for i in range(abs(index), size):
                    self.treeContent[i].move(self.master, self.treeContent[i].posx - 50, self.centery - 100)

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
        frameLbl = Label(self.frame, text='Tree display frame')
        frameLbl.pack(anchor='center')

        self.canvas.pack(fill='both', expand=True)

        self.root = Node(self.canvas)

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
