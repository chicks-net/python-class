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
		turtle.forward(200)
		turtle.left(60)

def hexagon(size):
	for _ in range(6):
		turtle.forward(size)
		turtle.left(60)

def hexagon2():
	for _ in range(3):
		hexagon()
		turtle.left(120)

def hexagon3():
	for _ in range(3):
		turtle.color("black")
		hexagon2()
		turtle.color("blue")
		turtle.forward(90)
		turtle.right(60)
		turtle.color("red")
		hexagon2()
		turtle.forward(90)
		turtle.right(60)

def polygon(sides,size):
	angle = 360/sides

	for _ in range(sides):
		turtle.forward(size)
		turtle.right(angle)

#square()
#hexagon3()
turtle.width(2)

for _ in range(6):
	polygon(5,80)
	turtle.left(60)

turtle.exitonclick()
