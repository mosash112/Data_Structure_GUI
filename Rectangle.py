from tkinter import Canvas, Label


class Rectangle:
    def __init__(self, master=Canvas):
        self.width = None
        self.height = None
        self.center = None
        self.shape = None
        self.posy = 0
        self.posx = 0
        self.move_step = 10
        self.valuelbl = None
        self.master = master
        self.after_id = None

    def draw(self, posx, posy, width, height, value=None, fill=None):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.shape = self.master.create_rectangle(posx - (width / 2), posy - (height / 2), posx + (width / 2),
                                                  posy + (height / 2), fill=fill)
        self.valuelbl = self.master.create_text(posx, posy, text=value, font=("Arial", 12), fill="white")
        # self.center = self.master.create_oval(posx - 3, posy - 3, posx + 3, posy + 3, fill="white")

    def move(self, root, targetx, targety):
        if self.after_id:
            self.master.after_cancel(self.after_id)
        self._move_to(root, targetx, targety)

    def _move_to(self, root, targetx, targety):
        if self.posx == targetx and self.posy == targety:
            return
        else:
            currentx = self.posx
            currenty = self.posy
            stepx = (targetx - currentx) / self.move_step
            stepy = (targety - currenty) / self.move_step
            if currentx != targetx:
                self.posx += stepx
            if currenty != targety:
                self.posy += stepy
            self.master.move(self.shape, stepx, stepy)
            self.master.move(self.valuelbl, stepx, stepy)
            # print("currentx, currenty: ", currentx, currenty)
            # print("targetx, targety: ", targetx, targety)
            self.after_id = root.after(100, self.move, root, targetx, targety)

    def destroy(self):
        self.master.delete(self.shape)
        self.master.delete(self.center)
        self.master.delete(self.valuelbl)
        # self.destroy()
