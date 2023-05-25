"""
Python 3 program to calculate the Standard Deviation

Task: Given an array, arr, of n integers, calculate and print the
standard deviation. Your answer should be in decimal form, rounded
to a scale of 1 decimal place (i.e., 12.3 format). An error margin
of +/- 0.1 will be tolerated for the standard deviation.

Sample input: 
n = 5
arr = 10 40 30 50 20

Expected output:
Standard Deviation: 14.1
"""

#Import libraries
import math

#Mean
def mean(n, arr):
    return sum(arr) / n

#Standard Deviation
def stdDev(n, arr):
    s = 0
    #Subtract the mean from each element, square each result, and take their sum
    for i in range(n):
        s += (arr[i] - mean(n, arr)) ** 2
    #Take the square root using Python's math.sqrt() Method
    return math.sqrt(s / n)
            
#Main 
def main():
    #User input for the length of the array
    n = int(input())
    
    #User input for the elements of the array
    arr = list(map(int, input().strip().split()))[:n]
    
    #Standard Deviation
    std_dev_result = stdDev(n, arr)
    
    #Print the output for the Standard Deviation
    print("%.1f" % std_dev_result)
    
#To run main() function
if __name__ == "__main__":
    main()
