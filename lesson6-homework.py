#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
https://greatscottgadgets.com/sdr/6/
homework
A weather station measures wind direction once per minute. Write a program to indicate the average direction over a five minute period. Try it on the following sets of readings:
12°, 15°, 13°, 9°, 16°
358°, 1°, 359°, 355°, 2°
210°, 290°, 10°, 90°, 170°
Modify your program to handle wind speed input in addition to direction.
'''

list = [358, 10, 1, 10, 359, 5, 355, 5, 2, 10]
dTotal = 0
wTotal = 0


for index, value in enumerate(list):
    if index % 2 == 0:
        dTotal += value
    else:
        wTotal+= value

direction = dTotal/(len(list)/2)
windspeed = wTotal/(len(list)/2)

print "Average wind direction is: %s\nAverage windspeed is : %s" % (direction, windspeed)
