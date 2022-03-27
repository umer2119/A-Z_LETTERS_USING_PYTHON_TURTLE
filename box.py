# from itertools import count
from turtle import *

def box(count):
    penup()
    forward(40)
    left(90)
    forward(40)
    pendown()
    left(90)
    forward(count*160)
    left(90)
    forward(200)
    left(90)
    forward(count*160)
    left(90)
    forward(200)


# box(4)
# done()