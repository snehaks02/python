from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import math

window_size = 600
scale = 100

xc = yc = 0
r = 50


def init_display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glPointSize(20)


def midpoint_circle():
    glBegin(GL_POINTS)
    global xc, yc, r
    p = 1 - r
    x, y = 0, r
    plot_symmetric_points(x, y)
    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x - 2 * y + 1
        plot_symmetric_points(x, y)
    glEnd()
    glFlush()


def plot_symmetric_points(x, y):
    global xc, yc
    glVertex2f((xc + x) / scale, (yc + y) / scale)
    # glVertex2f((xc + x) / scale, (yc - y) / scale)
    glVertex2f((xc - x) / scale, (yc - y) / scale)
   # glVertex2f((xc - x) / scale, (yc + y) / scale)
    glVertex2f((xc + y) / scale, (yc + x) / scale)
    #glVertex2f((xc + y) / scale, (yc - x) / scale)
    #glVertex2f((xc - y) / scale, (yc + x) / scale)
    glVertex2f((xc - y) / scale, (yc - x) / scale)


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("circle")
    glutDisplayFunc(midpoint_circle)
    glutMainLoop()

main()
