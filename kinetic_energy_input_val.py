#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
August
"""
# Fuction to load the steps.txt file
def tracker():
    steps_data = open('C:/Users/augus/Documents/MATH 6380/Homeworks/HW-3/steps.txt','r') 
    data = steps_data.readlines()
    start = 0
    months_lenght = [31,28,31,30,31,30,31,31,30,31,30,31]
    print('{:<7s} {:<10s} {:<10s} {:<10s}'.format('Month', 'Average','Minimum',"Maximum"))

# Loop to calculate the number of average. max and min steps per month
    for month in range(12): #loop throu data tp define intervals equal to each month's length
        lenght = start + months_lenght[month] #each month start where the previous month ends
        steps = data[start:lenght]  #steps for each month are defined at each iteration
        #print(steps)
        ave = 0         ####################################################
        maxi = 0        ### Descriptive stats computed at each iteration ###
        mini = 0        ####################################################
        for ste in steps:           #loop throu steps to compute descriptives
            ave = ave + float(ste)
            ste = int(ste)
            if mini == 0 or mini > ste:
                mini = ste
            if maxi == 0 or maxi < ste:
                maxi = ste
        ave = ave/len(steps)
        
        steps_data.close() 
        print('{:<7d} {:<10.2f}{:<10d}{:<10d}'.format(month+1, ave, mini, maxi))
        start = start+months_lenght[month]  #Print descriptive at each iteration

tracker()

