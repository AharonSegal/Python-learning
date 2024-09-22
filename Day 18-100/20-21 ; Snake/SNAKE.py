from turtle import Screen,Turtle

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")

starting_point = [(-40,0) ,(-20,0), (0,0)]

for position in starting_point:
    snake = Turtle(shape="square")
    snake.color("white")
    snake.goto(position)


screen.exitonclick()