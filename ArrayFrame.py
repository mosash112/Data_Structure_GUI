from tkinter import *
from tkinter.ttk import *
from Rectangle import Rectangle


class ArrayFrame(Frame):
    def __init__(self, master=None, home_frame=None, array_size=0, width=0, height=0):
        super().__init__(master, height=height, width=width)
        self.master = master
        self.array_size = array_size
        self.height = height
        self.width = width
        self.centerx = self.width / 2
        self.centery = self.height / 2
        self.arrayContent = []
        self.frame = Frame(self.master)
        self.canvas = Canvas(self.frame, bg="#d0d0d0", height=self.height - 100,
                             width=self.width - 15)
        self.errlbl = Label(self.frame, text='')
        self.homeFrame = home_frame

    def insert(self, value, index=''):
        size = len(self.arrayContent)
        if size == self.array_size:
            print('array is full try updating instead')
            self.errlbl.config(text='array is full try updating instead', foreground='red')
            return

        newElement = Rectangle(self.canvas)
        print(index)
        if index == '':
            print('index was empty')
            index = size
            self.arrayContent.append(newElement)
            newElement.draw(self.centerx - 250, self.centery, 50, 50, value, 'green')
            newElement.move(self.master, self.centerx - (25 * (self.array_size - 1)) + (50 * index), self.centery - 100)
        else:
            index = int(index)
            if size > index:
                print('index was within the size')
                self.shift_elements(index)
                self.arrayContent.insert(index, newElement)
                newElement.draw(self.centerx - 250, self.centery, 50, 50, value, 'green')
                newElement.move(self.master, self.centerx - (25 * (self.array_size - 1)) + (50 * index),
                                self.centery - 100)
            else:
                print('index is bigger the size')
                self.arrayContent.append(newElement)
                newElement.draw(self.centerx - 250, self.centery, 50, 50, value, 'green')
                newElement.move(self.master, self.centerx - (25 * (self.array_size - 1)) + (50 * size),
                                self.centery - 100)

    def shift_elements(self, index):
        size = len(self.arrayContent)
        if size >= 1:
            if index > 0:
                for i in range(abs(index), size):
                    self.arrayContent[i].move(self.master, self.arrayContent[i].posx + 50, self.arrayContent[i].posy)
            elif index < 0:
                for i in range(abs(index), size):
                    self.arrayContent[i].move(self.master, self.arrayContent[i].posx - 50, self.arrayContent[i].posy)

    def update_element(self, value, index):
        if index == '':
            print('must enter an index')
            self.errlbl.config(text='must enter an index', foreground='red')
            return
        size = len(self.arrayContent)
        index = int(index)
        if size > index:
            print('size: ', size, 'index: ', index)
            newElement = Rectangle(self.canvas)
            self.arrayContent[index] = newElement
            newElement.draw(self.centerx - 250, self.centery, 50, 50, value, 'green')
            newElement.move(self.master, self.centerx - (25 * (self.array_size - 1)) + (50 * index),
                            self.centery - 100)
        else:
            print('index out of range')
            self.errlbl.config(text='index out of range', foreground='red')
            return

    def delete(self, index):
        size = len(self.arrayContent)
        if size == 0:
            print('array is empty')
            self.errlbl.config(text='array is empty', foreground='red')
            return
        if size > index:
            removed = self.arrayContent.pop(index)
            self.shift_elements(-index)
            if removed is not None:
                removed.destroy()
            print(size, self.arrayContent)
        else:
            print('index out of range')
            self.errlbl.config(text='index out of range', foreground='red')
            return

    def initialize(self):
        # for i in range(self.array_size):
        #     self.arrayContent.append(None)

        # display frame components
        frame2Lbl = Label(self.frame, text='Array display frame')
        frame2Lbl.pack(anchor='center')

        self.canvas.pack(fill='both', expand=True)

        arrayBody = Rectangle(self.canvas)
        arrayBody.draw(self.centerx, self.centery - 100, self.array_size * 50, 50, None, 'yellow')

        entryFrame = Frame(self.frame)
        btnFrame = Frame(self.frame)
        valueEntry = Entry(entryFrame)
        valueEntry.pack(side=LEFT)
        indexEntry = Entry(entryFrame)
        indexEntry.pack(side=LEFT)
        insertBtn = Button(btnFrame, text='Insert',
                           command=lambda: [self.insert(valueEntry.get(), indexEntry.get())])
        insertBtn.pack(side=LEFT)
        updateBtn = Button(btnFrame, text='Update',
                           command=lambda: [self.update_element(valueEntry.get(), indexEntry.get())])
        updateBtn.pack(side=LEFT)
        deleteBtn = Button(btnFrame, text='Delete', command=lambda: [self.delete(int(indexEntry.get()))])
        deleteBtn.pack(side=LEFT)
        self.errlbl.pack(side=LEFT)
        entryFrame.pack()
        btnFrame.pack()

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
