#!/usr/bin/python

import turtle

line_size = 6
angle = 45;

while True:
	turtle.forward(line_size)
	line_size += 3
	turtle.left(angle)
	turtle.width( int( line_size/8 ) )

	if turtle.distance(0,0) > 200:
		break
	

turtle.exitonclick()
