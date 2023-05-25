"""
Python 3 program to calculate Pearson Correlation Coefficient

Task: Given two n-element data sets, X and Y, calculate the value
of the Pearson correlation coefficient.

Sample input: 
n = 10
x = 10 9.8 8 7.8 7.7 7 6 5 4 2
y = 200 44 32 24 22 17 15 12 8 4

Expected output:
Pearson Correlation Coefficient: 0.612
"""
#Import libraries
import math

#Mean
def mean(n, arr):
    return sum(arr) / n

#Standard Deviation
def std_dev(n, arr):
    s = 0
    for i in range(n):
        s += (arr[i] - mean(n, arr)) ** 2
    return math.sqrt(s / n)

#Covariance
def covariance(n, x, y):
    #Calculate the Mean for data set X
    x_mean = mean(n, x)
    #Calculate the Mean for data set Y
    y_mean = mean(n, y)

    #Calculate Covariance for data sets X and Y
    covariance = 0
    for i in range(n):
        covariance += (x[i] - x_mean) * (y[i] - y_mean)
    covariance = (1 / n) * covariance
    
    return covariance

#Pearson Correlation Coefficient
def pearson(n, x, y):
    #Calculate Standard Deviation for data set X
    x_std = std_dev(n, x)
    #Calculate Standard Deviation for data set Y
    y_std = std_dev(n, y)
    
    #Calculate Pearson Correlation Coefficient for data sets X and Y
    pearson = covariance(n, x, y) / (x_std * y_std)
    
    return pearson

#Main
def main():
    #User input for the size of data sets X and Y
    n = int(input())
    
    #User input for the elements of data set X
    x = list(map(float, input().split())) 
    
    #User input for the elements of data set Y
    y = list(map(float, input().split()))
    
    #Calculate Covariance for data sets X and Y
    covariance_result = covariance(n, x, y)
    
    #Calculate Pearson Correlation Coefficient for data sets X and Y
    pearson_result = pearson(n, x, y)
    
    #Print the output for Pearson Correlation Coefficient
    print("%.3f" % pearson_result)
    
#To run main() function   
if __name__ == "__main__":
    main()
