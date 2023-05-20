"""
Python 3 program to calculate Mean, Median, Mode by defining functions (Version 1)

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
from collections import Counter

#Mean 
def mean(elements, length):
    return sum(elements) / length 

#Median
def median(elements, length):
    if length % 2 == 0:
        return (elements[length//2] + elements[length//2 - 1])/2

    return elements[length//2]

#Mode
def mode(elements, length):
    data = Counter(elements)
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

    if len(mode) == length or len(mode) >= 2:
        return min(mode)

    mode = ', '.join(map(str, mode))

    return mode

#Main
def main():
    #User input for the length of the array
    length = int(input())
    
    #User input for the elements of the array
    elements = list(map(int, input().strip().split()))[:length]
    
    #Sort the elements in the array
    elements.sort()

    #Calculate the Mean of the elements
    mean_result = mean(elements, length)

    #Calculate the Median of the elements
    median_result = median(elements, length)

    #Calculate the Mode of the elements
    mode_result = mode(elements, length)

    #Print the output for the Mean, Median, Mode
    print("%.1f" % mean_result)
    print("%.1f" % median_result)
    print(mode_result)

#To run main() function
if __name__ == "__main__":
    main()
