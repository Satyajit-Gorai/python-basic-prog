# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 18:25:37 2020

@author: Satyajit Gorai
"""

fw = open('simple.txt','w')
fw.write('this is a test file and it is for test purposes')
fw.close()

fr = open('simple.txt', 'r')
text = fr.read()
print(text)
fr.close()