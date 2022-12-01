from phys1d.physics import Obj
from phys1d.ext import truncate
from graphics import *
import math

print("1D Physics, for standard drop test, input: p = 400, v = 0, a = -98")
#p = int(input("Initial position (int, between 0-400 for on screen): "))
#v = int(input("Initial velocity (int): "))
#a = int(input("Gravity (int, default is -98): "))

p=200
v=0
a=-98


ball = Obj(p, v, a)

x, y = 300, 500
win = GraphWin("Hello", x, y, autoflush=False)


class Obj:

    def __init__(self, position, velocity, acceleration=-98):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.bounce = 0.6

    def __repr__(self):
        return f"Pos: {self.position}, Spd: {self.velocity}, Acc: {self.acceleration}"

    def p_update(self, time):
        self.prev_position = self.position
        self.position += self.velocity * time

    def v_update(self, time):
        self.prev_velocity = self.velocity

        if self.position >= 0:
            self.velocity += self.acceleration * time
        else:
            self.velocity *= -1 * self.bounce
            self.position = 0

    def update(self, time):
        self.v_update(time)
        self.p_update(time)

def truncate(number, decimals=0):
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer.")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more.")
    elif decimals == 0:
        return math.trunc(number)

    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor

def clearscreen(window):
    for i in (window.find_all()):
        window.delete(i)


def update_object(window):
    obj = Circle(Point(150, - ball.position + 430), 20)
    obj.draw(window)


def update_background(window):
    b = Line(Point(-100, 450), Point(300, 450))
    b.draw(window)


def text(window):
    info = Text(Point(70, 30), f"y-pos: {truncate(ball.position, 2)} \n"
                               f"speed: {truncate(ball.velocity, 2)} \n"
                               f"acceleration : {truncate(ball.acceleration, 2)}")
    info.setTextColor(color_rgb(0, 0, 0))
    info.setSize(15)
    info.setFace('times roman')

    info.draw(window)


def frame(fps):
    ball.update(1 / fps)

    clearscreen(win)

    text(win)
    update_object(win)
    update_background(win)
    update(fps)


def main():
    while True:
        frame(120)


if __name__ == '__main__':
    main()

win.getMouse()
