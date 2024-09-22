from turtle import Turtle as t, Screen
import random

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

tim = t()

def draw_shapes(angle_num):
    angle = 360 / angle_num
    for _ in range(angle_num):
        tim.forward(100)
        tim.right(angle)

for shape_side in range(3, 11):
    selected_color = random.choice(colours)
    tim.color(selected_color)
    draw_shapes(shape_side)
    colours.remove(selected_color)



screen = Screen()
screen.exitonclick()
