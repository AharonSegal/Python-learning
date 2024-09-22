import turtle as t
import random

tim = t.Turtle()
t.colormode(255)

tim.pos(0,50)

def generate_pastel_color():
    # Generate random values for pastel-like red, green, and blue components
    red = random.randint(150, 255)
    green = random.randint(150, 255)
    blue = random.randint(150, 255)
    return (red,green,blue)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90,90,90,45, 270]
tim.pensize(15)
tim.speed("fastest")

for i in range(9999999999):
    tim.forward(random.randint(10,30))
    tim.right(random.choice(directions))
    tim.color(generate_pastel_color())