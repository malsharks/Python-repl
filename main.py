import turtle
import random

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("square")
player_one.penup()
player_one.goto(-200, 100)
player_two = player_one.clone()
player_two.color("red")
player_two.penup()
player_two.goto(-200, 100)

player_one
player_one