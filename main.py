Question = '''
Make a function that draws a right triangle with two non-hypotenuse sides as its inputs.

hint: might need modules: turtle, math'''

from math import *
from turtle import *
def makeDegrees(radians):
    return 180*radians/pi
def rightTriangle(s1, s2):
    fd(s1)
    seth(90+makeDegrees(atan(s1/s2)))
    fd(sqrt(s1*s1+s2*s2))
    seth(-90)
    fd(s2)
rightTriangle(300,400)
exitonclick()