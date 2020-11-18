# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 01:45:09 2020

@author: anves
"""

from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()
