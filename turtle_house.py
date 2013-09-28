#!/usr/bin/python

import turtle
import math

turtle.shape("turtle")
turtle.width(2)

# square
right_angle=90
square_size=140

turtle.forward(square_size)
turtle.left(right_angle)
turtle.forward(square_size)
turtle.left(right_angle)
turtle.forward(square_size)
turtle.left(right_angle)
turtle.forward(square_size)
turtle.left(right_angle)

# diaganals
diaganal_size = math.sqrt( 2 * (square_size ** 2) )

turtle.color("red")
turtle.left(right_angle/2)
turtle.forward(diaganal_size)
turtle.color("black")
turtle.left(3* (right_angle/2) )
turtle.forward(square_size)
turtle.color("blue")
turtle.left(3* (right_angle/2) )
turtle.forward(diaganal_size)

# get back to upper right corner of square
turtle.left(3* (right_angle/2) )
turtle.color("black")
turtle.forward(square_size)
turtle.color("green")

# triangle
triangle_size = square_size
turtle.left(right_angle/2)
turtle.forward(triangle_size)
turtle.left(right_angle)
turtle.forward(triangle_size)

#turtle.color("red")
#turtle.color("green")
#turtle.color("blue")

turtle.exitonclick()
