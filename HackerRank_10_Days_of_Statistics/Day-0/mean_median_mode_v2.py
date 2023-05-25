"""
Python 3 program to calculate Mean, Median, Mode using built-in libraries (Version 2)

Task: Given an array, X, of N integers, calculate and print the respective mean, 
median, and mode on separate lines. If your array contains more than one modal 
value, choose the numerically smallest one. 

Note: Other than the modal value (which will always be an integer), your answers 
should be in decimal form, rounded to a scale of 1 decimal place.

Sample input: 
Length: 10
Elements: 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

Expected output:
Mean: 43900.6
Median: 44627.5
Mode: 4978
"""

#Import libraries
import numpy as np
from scipy import stats

#User input for the length of the array
length = int(input())

#User input for the elements of the array
elements = list(map(int, input().strip().split()))[:length]

#Calculate the Mean of the elements
mean_result = np.mean(elements)

#Calculate the Median of the elements
median_result = np.median(elements)

#Calculate the Mode of the elements
mode_result = int(stats.mode(elements)[0])

#Print the output for the Mean, Median, Mode
print("%.1f" % mean_result)
print("%.1f" % median_result)
print(mode_result)
