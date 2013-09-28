#!/usr/bin/python

import turtle

dash_size=10
space_size=3

for y in range(9):
	turtle.forward(dash_size + 3*y)
	turtle.penup()
	turtle.forward(space_size)
	turtle.pendown()

turtle.forward(dash_size)
turtle.shape("arrow")

# wait 
turtle.exitonclick()
