import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")



def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

########### Challenge 5 - Spirograph ########

for i in range(200):
    tim.circle(50)
    tim.right(10)
    tim.color(random_color())




