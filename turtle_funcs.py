#!/usr/bin/python

import turtle

def line_without_moving():
    turtle.forward(50)
    turtle.backward(50)

def square():
	for _ in range(4):
		turtle.forward(90)
		turtle.left(90)

def hexagon():
	for _ in range(6):
		turtle.forward(90)
		turtle.left(60)

def hexagon2():
	for _ in range(3):
		hexagon()
		turtle.left(120)

#square()
hexagon2()


turtle.exitonclick()
