#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 27 10:06:21 2023

@author: justin
"""

# import neccessary libraries required for the plotting of a graph, such as matplotlib
import matplotlib.pyplot as plt

#list of x-values and y-values we want to plot
y = [0.21,0.41,0.58,0.79,1.00,1.18,1.37,1.58,1.74,1.95]
x = [10,20,30,40,50,60,70,80,90,100]

#the plot() function creates the plot
plt.plot(x,y) #make sure that the x and the y list contains same number of elements

#xlabel() and ylabel() functions helps in renameing the titles of x and y axis
plt.xlabel('Step (10 mb/step)')
plt.ylabel('Time')

#includes the title of graph using title() function
plt.title('CPU Time vs File Size')

#saves the graph as a file
plt.savefig("COEN146_Lab1.png")

#shows output of the graph on the screen
plt.show()