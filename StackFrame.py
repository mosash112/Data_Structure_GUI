from tkinter import *
from tkinter.ttk import *
from Rectangle import Rectangle


class StackFrame(Frame):
    def __init__(self, master=None, home_frame=None, stack_size=0, width=0, height=0):
        super().__init__(master, height=height, width=width)
        self.master = master
        self.stack_size = stack_size
        self.height = height
        self.width = width
        self.centerx = self.width / 2
        self.centery = self.height / 2
        self.stackContent = []
        self.frame = Frame(self.master)
        self.canvas = Canvas(self.frame, bg="#d0d0d0", height=self.height - 100,
                             width=self.width - 15)
        self.errlbl = Label(self.frame, text='')
        self.homeFrame = home_frame

    def push(self, value=None, pos = 0, errlbl=None):
        size = len(self.stackContent)
        if size == self.stack_size:
            print('stack is full')
            self.errlbl.config(text='stack is full', foreground='red')
            return
        newElement = Rectangle(self.canvas)
        newElement.draw(self.centerx - 150, self.centery+100, 50, 50, value, 'green')
        newElement.move(self.master, self.centerx , self.centery + 200 - (50 * (self.stack_size - 2 + len(self.stackContent))))
        # self.shift_elements(newElement)
        self.stackContent.append(newElement)

    def pop(self):
        size = len(self.stackContent)
        if size == 0:
            print('stack is empty')
            self.errlbl.config(text='stack is empty', foreground='red')
            return
        lastElement = self.stackContent.pop()
        lastElement.move(self.master, self.centerx+150, self.centery +100)

    def shift_elements(self, newElement):
        size = len(self.stackContent)
        if size >= 1:
            for i in range(size):
                self.stackContent[i].move(self.master, self.stackContent[i].posx, self.stackContent[i].posy)
        self.stackContent.insert(0, newElement)

    def initialize(self):
        # display frame components
        frameLbl = Label(self.frame, text='Stack display frame')
        frameLbl.pack(anchor='center')

        self.canvas.pack(fill='both', expand=True)

        stackBody = Rectangle(self.canvas)
        stackBody.draw(self.centerx, self.centery-50,  50, self.stack_size * 50, None, 'yellow')

        inputFrame = Frame(self.frame)
        valueEntry = Entry(inputFrame)
        valueEntry.pack(side=LEFT)
        pushBtn = Button(inputFrame, text='Push', command=lambda: [self.push(valueEntry.get())])
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
