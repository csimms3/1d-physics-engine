from phys1d.physics import Obj
from ext import truncate
from graphics import *

'''print("1D Physics, for standard drop test, input: p = 400, v = 0, a = -98")
p = int(input("Initial position (int, between 0-400 for on screen): "))
v = int(input("Initial velocity (int): "))
a = int(input("Gravity (int, default is -98): "))'''

objectlist = []
ball1 = Obj(400, 0, -400, 0.5)


objectlist.append(ball1)




x, y = 300, 500
win = GraphWin("Hello", x, y, autoflush=False)


def clearscreen(window):
    for obj in (window.find_all()):
        window.delete(obj)


def update_object(window, rate):
    for obj in objectlist:

        obj.update(1/rate)

        item = Circle(Point(150, - obj.position + 430), 20)
        item.draw(window)


def update_background(window):
    b = Line(Point(-100, 450), Point(300, 450))
    b.draw(window)


def text(window):
    info = Text(Point(70, 30), f"y-pos: {truncate(ball1.position, 2)} \n"
                               f"speed: {truncate(ball1.velocity, 2)} \n"
                               f"acceleration : {truncate(ball1.acceleration, 2)}")
    info.setTextColor(color_rgb(0, 0, 0))
    info.setSize(15)
    info.setFace('times roman')

    info.draw(window)


def frame(fps):
    clearscreen(win)

    text(win)
    update_object(win, fps)
    update_background(win)
    update(fps)


def main():
    while True:
        frame(120)


if __name__ == '__main__':
    main()

win.getMouse()
