import turtle

class Pen(turtle.Turtle):
    
    def __init__(self, shape = "classic", undobuffersize = 1000, visible = False):
        super().__init__(shape, undobuffersize, visible)
        self.color("black")
        self.pu()
        self.goto(0,0)

    def enter(self,input, x_coor, y_coor,size):
        self.goto(x_coor, y_coor)
        self.write(input, align="center", font=("Arial", size, "normal"))
    