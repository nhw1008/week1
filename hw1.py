from turtle import *
import random

class Car:
    def __init__(self, speed, color, fname, start_x, start_y):
        self.speed = speed
        self.color = color
        self.turtle = Turtle()
        self.turtle.shape(fname)
        self.turtle.penup()
        self.turtle.goto(start_x, start_y)
        self.turtle.setheading(90)  # 12시 방향

    def drive(self):
        self.turtle.forward(self.speed)

register_shape("car1.gif")
register_shape("car2.gif")

car_list = [
    Car(random.randint(5, 15), "red", "car1.gif", -100, -200),
    Car(random.randint(5, 15), "blue", "car2.gif", 0, -200),
    Car(random.randint(5, 15), "green", "car1.gif", 100, -200)
]

race_on = True
while race_on:
    for car in car_list:
        car.drive()
        if car.turtle.ycor() >= 200:
            race_on = False
            break

done()
