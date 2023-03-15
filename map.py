from turtle import Turtle


class Map(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.x = 0
        self.y = 0
        self.state = ""

    def update_map(self):
        self.goto(self.x, self.y)
        self.write(self.state, align="center", font=("Courier", 12, "normal"))

    def add_point(self):
        self.score += 1
        self.update_map()
