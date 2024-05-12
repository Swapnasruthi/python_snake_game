import turtle as t
import time
from snake import Snake
from food import Food
from score_board import Score_board
swap=0

tim=t.Turtle()
screen=t.Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("MY SNAKE GAME")
screen.tracer(0)


snake=Snake()
food=Food()
score_board = Score_board()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)

is_race_on = True
while is_race_on:
    screen.update()
    time.sleep(0.1)
    snake.move()




    #detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extent()
        score_board.increment_score()

    #detect collision with wall
    if snake.segments[0].xcor()>290 or snake.segments[0].xcor()<-290 or snake.segments[0].ycor()>290 or snake.segments[0].ycor()<-290:
        is_race_on=False
        score_board.game_over()


    #detect collision with tail
    for seg in snake.segments:
        swap=swap+1
        if seg == snake.segments[0]:
            pass
        elif snake.segments[0].distance(seg) < 10 and swap>3:
            is_race_on=False
            score_board.game_over()

print(f"your score is {score_board.score}")


screen.exitonclick()