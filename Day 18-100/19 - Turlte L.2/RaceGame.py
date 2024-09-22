from turtle import Turtle, Screen
import random


is_race_on = False
new_turtle = Turtle()
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:\n Red, Orange, Yellow, Green, Blue, Indigo, Violet ")
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
y_positions = [100,70,40,10,-20,-50,-80]
new_turtle.hideturtle()
all_turtles = []

for turtles in range(0,7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtles])
    new_turtle.penup()
    y_pos = y_positions[turtles]
    new_turtle.goto(-230,y=y_pos)
    new_turtle.pendown()
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")


        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()

