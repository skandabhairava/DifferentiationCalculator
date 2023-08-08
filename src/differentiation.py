#!/usr/bin/env python3
import turtle
import math
from typing import Callable

def draw_func(function, turtle: turtle.Turtle, x: int, dx):
    turtle.penup()
    turtle.goto(-1000, function(-1000))

    turtle.pendown()
    for x_pos in range(-1000, 1000):
        result = function(x_pos)
        turtle.goto(x_pos, result)
        turtle.dot(1)

    turtle.penup()

    result = function(x)

    slope_at_x = ((function(x+dx) - result)/((x+dx) - (x)))
    tangent = lambda x_tangent: (slope_at_x * (x_tangent - x)) + result

    turtle.goto(x - 50, tangent(x - 50))
    turtle.color("blue")
    turtle.pendown()
    for x_pos in range(x-50, x+50):
        res = tangent(x_pos)
        turtle.goto(x_pos, res)
        turtle.dot(1)

    turtle.penup()

    return slope_at_x

def main(function, dx, x):
    if (dx == 0):
        return

    differentiation = turtle.Turtle()
    screen = turtle.Screen()

    turtle.color("black", "black")
    screen.screensize(5000, 5000)

    axis = turtle.Turtle()
    axis.color("red3")
    for i in range(-1, 2):
        axis.goto(i*3000, 0)
    axis.home()
    for i in range(-1, 2):
        axis.goto(0, i*3000)

    axis.shapesize(0.1, 5)
    axis.shape("square")
    axis.pu()

    slope = draw_func(function, differentiation, x, dx)
    print(f"Slope at given point x={x} is ~{round(slope, 3)}")

if __name__ == "__main__":
    turtle.tracer(0)
    turtle.speed(0)

    differentiating_func: Callable = lambda x: 2 * ((x/10)**3) + 3 * ((x/10)**2) + 5
    at_x = 20

    main(differentiating_func, 0.000001, at_x)
    turtle.exitonclick()