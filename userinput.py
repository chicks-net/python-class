#!/usr/bin/python

import turtle

def polygon(sides,size):
	angle = 360/sides

	for _ in range(sides):
		turtle.forward(size)
		turtle.right(angle)

direction = raw_input("angle? ")

turtle.width(2)

for _ in range(6):
	polygon(5,80)
	turtle.left(int(direction))

turtle.exitonclick()
