from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        x_cor=random.randint(-280,280)
        y_cor=random.randint(-280,280)
        self.goto(x_cor,y_cor)
    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)

    def special_food(self):
        self.color("white")
        self.shapesize(stretch_len=1,stretch_wid=1)

    def food_normal(self):
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)










#
# import turtle as t
# import random
#
# class Food():
#     def __init__(self):
#         f=t.Turtle(shape="circle")
#         f.penup()
#         f.color("blue")
#         f.shapesize(stretch_len=0.5,stretch_wid=0.5)
#         x_cor=random.randint(-280,280)
#         y_cor=random.randint(-280,280)
#         f.goto(x_cor,y_cor)