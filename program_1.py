# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year, 
# the average monthly rainfall, # and the months with the highest and lowest amounts.

#Tanner Rosenthal
#2/28/2025
#Rainfall Calculator

import statistics
rainfall_list = []

for rainfall in range(1,13):
    rain = int(input(f"How much did it rain in month {rainfall}?"))
    rainfall_list.append(rain)

avg = sum(rainfall_list)/len(rainfall_list)
print(max(rainfall_list), "is the highest amount it rained in a month")
print(min(rainfall_list), "is the lowest amount it rained in a month")
print(f"The average rainfall was {avg:.2f}")

