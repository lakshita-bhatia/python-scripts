#!/usr/bin/python
import turtle

brad = turtle.Turtle()
def mk_square():
	for a in range(4):
		brad.forward(100)
		brad.right(90)

def draw_square():
	window = turtle.Screen()
	window.bgcolor("red")

	brad.shape("turtle")
	brad.color("black")
	brad.speed(0.2)
	for i in range(60):
		mk_square()
		brad.right(6)
#	angie = turtle.Turtle()
#	angie.shape("arrow")
#	angie.color("blue")
#	angie.circle(100)
	window.exitonclick()

draw_square()
