# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 19:23:30 2020

@author: Satyajit Gorai
"""

import turtle

p =  turtle.Turtle()

p.pensize(3)
p.pencolor("blue")
for i in range(4):
    p.forward(100)
    p.right(90)


p.right(45)
p.forward(42.426)
p.left(45)

for i in range(4):
    p.forward(100)
    p.right(90)

p.forward(100)
p.left(135)
p.forward(42.426)
p.left(135)
p.forward(100)
p.left(45)
p.forward(42.426)
p.right(135)
p.forward(100)
p.right(45)
p.forward(42.426)



turtle.done()
