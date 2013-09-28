#!/usr/bin/python

import turtle

def line_without_moving():
    turtle.forward(50)
    turtle.backward(50)

for _ in range(3):
	line_without_moving()
	turtle.right(90)

line_without_moving()

turtle.exitonclick()
