from OpenGL.GL import*
from OpenGL.GLU import*
from OpenGL.GLUT import*
import math
import numpy as np
import sys
window_size=600
scale=100
xc=yc=0
r=10
point=10



def init():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)

def set_pixel(x,y,color=(1,0,1)):
    glColor3f(*color)
    glPointSize(point)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()
    glFlush()

def get_pixel(x,y):
    pixel=glReadPixels(x,window_size-y,1,1,GL_RGB,GL_FLOAT)
    return pixel[0][0]

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    gluOrtho2D(0,window_size,window_size,0)
    xc=window_size/2
    yc=window_size/2
    a=150
    b=80
    ellipse(xc,yc,a,b)
    glFlush()

def ellipse(xc,yc,a,b):
    theta=2*math.pi
    while theta>=0:
        x=a*math.cos(theta)
        y=b*math.sin(theta)
        set_pixel(x+xc,y+yc)
        theta-=0.001


def boundary_fill(x,y,new_color,boundary_color):
    color=get_pixel(x,y)
    if list(color)!=list(new_color) and list(color)!=boundary_color:
        set_pixel(x,y,new_color)
        boundary_fill(x+point,y,new_color, boundary_color)
        boundary_fill(x,y+point,new_color, boundary_color)
        boundary_fill(x-point,y,new_color,boundary_color)
        boundary_fill(x,y-point,new_color, boundary_color)





def mouse_pointer(button,state,x,y):
    if button==GLUT_LEFT_BUTTON and state==GLUT_DOWN:
        boundary_fill(x,y,(1,1,0),(1,0,1))


def main():
    glutInit()
    glutInitWindowSize(window_size, window_size)
    glutCreateWindow("ellipse")
    glutDisplayFunc(display)
    glutMouseFunc(mouse_pointer)
    glutMainLoop()
main()
