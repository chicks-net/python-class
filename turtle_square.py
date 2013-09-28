#!/usr/bin/python

import turtle

turtle.shape("turtle")
turtle.width(2)

right_angle=90
square_size=140

turtle.forward(square_size)
turtle.left(right_angle)

turtle.color("red")
turtle.forward(square_size)
turtle.left(right_angle)

turtle.color("green")
turtle.forward(square_size)
turtle.left(right_angle)

turtle.color("blue")
turtle.forward(square_size)
turtle.left(right_angle)

turtle.exitonclick()
