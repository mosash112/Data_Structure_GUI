from tkinter import *
from tkinter.ttk import *

from ArrayFrame import ArrayFrame
from QueueFrame import QueueFrame
from StackFrame import StackFrame
from TreeFrame import TreeFrame

window_width = 600
window_height = 500
array_size = 7
centerx = (window_width/2)
centery = (window_height/2)


# a function that hide a frame
def hide_frame(frame):
    frame.pack_forget()


# a function that shows a frame
def show_frame(frame):
    frame.pack(fill="both", expand=True)


# a function that closes the whole window
def close_window():
    window.destroy()


# creating the window
window = Tk()
window.geometry(f"{window_width}x{window_height}")

# home frame components
homeFrame = Frame(window, height=window_height, width=window_width)
homeFrame.pack(fill='both', expand=True, anchor='center')

titleLbl = Label(homeFrame, text='welcome to data structure visualizer')
titleLbl.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

queueBtn = Button(homeFrame, text='Start queue', command=lambda: [hide_frame(homeFrame), show_frame(queueFrame),
                                                                  queueFrame.initialize()])
queueBtn.grid(row=1, column=0, padx=5, pady=5)

stackBtn = Button(homeFrame, text='Start stack', command=lambda: [hide_frame(homeFrame), show_frame(stackFrame),
                                                                  stackFrame.initialize()])
stackBtn.grid(row=2, column=0, padx=5, pady=5)

arrayBtn = Button(homeFrame, text='Start array', command=lambda: [hide_frame(homeFrame), show_frame(arrayFrame),
                                                                  arrayFrame.initialize()])
arrayBtn.grid(row=1, column=2, padx=5, pady=5)

treeBtn = Button(homeFrame, text='Start tree', command=lambda: [hide_frame(homeFrame), show_frame(treeFrame),
                                                                treeFrame.initialize()])
treeBtn.grid(row=2, column=2, padx=5, pady=5)

exitBtn = Button(homeFrame, text='Exit', command=close_window)
exitBtn.grid(row=3, column=1, padx=5, pady=5)

# queue frame components
queueFrame = QueueFrame(window, homeFrame, array_size, window_width, window_height)

stackFrame = StackFrame(window, homeFrame, array_size, window_width, window_height)

arrayFrame = ArrayFrame(window, homeFrame, array_size, window_width, window_height)

treeFrame = TreeFrame(window, homeFrame, array_size, window_width, window_height)

# showing home frame and hiding display frame
show_frame(homeFrame)
hide_frame(queueFrame)
hide_frame(stackFrame)
hide_frame(arrayFrame)
hide_frame(treeFrame)

# starting the window
window.mainloop()
