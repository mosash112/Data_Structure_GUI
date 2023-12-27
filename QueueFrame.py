from tkinter import *
from tkinter.ttk import *
from Rectangle import Rectangle


class QueueFrame(Frame):
    def __init__(self, master=None, home_frame=None, queue_size=0, width=0, height=0):
        super().__init__(master, height=height, width=width)
        self.master = master
        self.queue_size = queue_size
        self.height = height
        self.width = width
        self.centerx = self.width / 2
        self.centery = self.height / 2
        self.queueContent = []
        self.frame = Frame(self.master)
        self.canvas = Canvas(self.frame, bg="#d0d0d0", height=self.height - 100,
                             width=self.width - 15)
        self.errlbl = Label(self.frame, text='')
        self.homeFrame = home_frame

    def enqueue(self, value=None, errlbl=None):
        size = len(self.queueContent)
        if size == self.queue_size:
            print('queue is full')
            errlbl.config(text='queue is full', foreground='red')
            return
        newElement = Rectangle(self.canvas)
        newElement.draw(self.centerx - 250, self.centery, 50, 50, value, 'green')
        newElement.move(self.master, self.centerx - (25 * (self.queue_size - 1)), self.centery - 100)
        self.shift_elements()
        self.queueContent.insert(0, newElement)

    def dequeue(self):
        size = len(self.queueContent)
        if size == 0:
            print('queue is empty')
            self.errlbl.config(text='queue is empty', foreground='red')
            return
        lastElement = self.queueContent.pop()
        lastElement.move(self.master, self.centerx + (25 * (self.queue_size + 4)), self.centery)

    def shift_elements(self):
        size = len(self.queueContent)
        if size >= 1:
            for i in range(size):
                self.queueContent[i].move(self.master, self.centerx - 100 + (50*i), self.centery - 100)

    def initialize(self):

        # display frame components
        frame2Lbl = Label(self.frame, text='Queue display frame')
        frame2Lbl.pack(anchor='center')

        self.canvas.pack(fill='both', expand=True)

        arrayBody = Rectangle(self.canvas)
        arrayBody.draw(self.centerx, self.centery - 100, self.queue_size * 50, 50, None, 'yellow')

        inputFrame = Frame(self.frame)
        valueEntry = Entry(inputFrame)
        valueEntry.pack(side=LEFT)
        enqueueBtn = Button(inputFrame, text='Enqueue', command=lambda: [self.enqueue(valueEntry.get())])
        enqueueBtn.pack(side=LEFT)
        dequeueBtn = Button(inputFrame, text='Dequeue', command=lambda: [self.dequeue()])
        dequeueBtn.pack(side=LEFT)
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
