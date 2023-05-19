#Python 3 program to calculate Mean, Median, Mode

"""
Task: Given an array, X, of N integers, calculate and print the respective mean, 
median, and mode on separate lines. If your array contains more than one modal 
value, choose the numerically smallest one. 
"""

#Import libraries
import numpy as np
from scipy import stats

#User input
"""
Sample input:
Length: 10
Elements: 64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
"""
length = int(input())
elements = list(map(int, input().strip().split()))[:length]

#Output
"""
Expected output:
Mean: 43900.6
Median: 44627.5
Mode: 4978
"""
#Mean
print(np.mean(elements))

#Median
print(np.median(elements))

#Mode
print(int(stats.mode(elements)[0]))
