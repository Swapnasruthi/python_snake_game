import turtle as t
SEGMENT_DISTANCE=[0,20,40]
SNAKE_DISTANCE=20
UP=90
LEFT=180
DOWN=270
RIGHT=0
class Snake():
    def __init__(self):
        self.segments=[]
        self.create_snake()
    def create_snake(self):
        for i in SEGMENT_DISTANCE:
            self.add_segment(i,0)
    def add_segment(self,position,y):
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position,y)
        self.segments.append(new_segment)
    def extent(self):
        x_cor=self.segments[-1].xcor()
        y_cor=self.segments[-1].ycor()
        self.add_segment(x_cor,y_cor)
    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            x_cor = self.segments[segment - 1].xcor()
            y_cor = self.segments[segment - 1].ycor()
            self.segments[segment].goto(x_cor, y_cor)
        self.segments[0].fd(SNAKE_DISTANCE)
    def up(self):
        if self.segments[0].heading()!=DOWN:
             self.segments[0].setheading(UP)
    def down(self):
        if self.segments[0].heading()!=UP:
            self.segments[0].setheading(DOWN)
    def left(self):
        if self.segments[0].heading()!=RIGHT:
            self.segments[0].setheading(LEFT)
    def right(self):
        if self.segments[0].heading()!=LEFT:
            self.segments[0].setheading(RIGHT)

