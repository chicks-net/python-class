#!/usr/bin/python

import turtle

turtle.width(2)

def maybe_forward(distance):
	if turtle.isdown():
		turtle.forward(distance)

turtle.color("red")
turtle.penup()
maybe_forward(30)

turtle.color("green")
turtle.pendown()
maybe_forward(30)

turtle.exitonclick()
