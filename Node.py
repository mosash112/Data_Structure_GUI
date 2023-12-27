from tkinter import Canvas, Label


class Node:
    def __init__(self, master=Canvas):
        self.radius = None
        self.center = None
        self.shape = None
        self.posy = 0
        self.posx = 0
        self.move_step = 10
        self.valuelbl = Label()
        self.master = master
        self.after_id = None

    def draw(self, posx, posy, radius, value=None, fill=None):
        self.posx = posx
        self.posy = posy
        self.radius = radius
        self.shape = self.master.create_oval(posx - self.radius, posy - self.radius, posx + self.radius,
                                             posy + self.radius, fill=fill)
        self.valuelbl = self.master.create_text(posx, posy, text=value, font=("Arial", 12), fill="white")

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
