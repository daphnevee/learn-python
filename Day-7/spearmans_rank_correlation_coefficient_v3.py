"""
Python 3 program to calculate Spearman's Rank Correlation Coefficient (Version 3)

Task: Given two n-element data sets, X and Y, calculate the value of
Spearman's rank correlation coefficient.

Note: If Rank X and Rank Y denote the respective ranks of each data point, then
the Spearman's rank correlation coefficient, rs, is the Pearson correlation
coefficient of Rank X and Rank Y.

Sample input: 
n = 10
x = 10 9.8 8 7.8 7.7 1.7 6 5 1.4 2
y = 200 44 32 24 22 17 15 12 8 4

Expected output:
Spearman's Rank Correlation Coefficient: 0.903
"""
#Import libraries
import math
import scipy.stats as ss

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
def covariance(n, p, q):
    #Calculate the Mean for data set X
    p_mean = mean(n, p)
    
    #Calculate the Mean for data set Y
    q_mean = mean(n, q)

    #Calculate Covariance for data sets X and Y
    covariance = 0
    for i in range(n):
        covariance += (p[i] - p_mean) * (q[i] - q_mean)
    covariance = (1 / n) * covariance
    
    return covariance

#Spearman's Rank Correlation Coefficient
def spearman(n, p, q):
    #Calculate the Standard Deviation for data set X
    p_std = std_dev(n, p)
    #Calculate the Standard Deviation for data set Y
    q_std = std_dev(n, q)
    
    #Calculate Spearman's Rank Correlation Coefficient (using Pearson)
    spearman = covariance(n, p, q) / (p_std * q_std)
    
    return spearman

#Main
def main():
    #User input for the no. of values in data sets X and Y
    n = int(input())
    
    #User input for the elements of data set X
    x = list(map(float, input().split())) 
    
    #User input for the elements of data set Y
    y = list(map(float, input().split()))
    
    #Rank the elements of data set X
    p = ss.rankdata(x)
    
    #Rank the elements of data set Y
    q = ss.rankdata(y)
    
    #Calculate Spearman's Rank Correlation Coefficient for data sets X and Y
    spearman_result = spearman(n, p, q)
    
    #Print the output for Spearman's Rank Correlation Coefficient
    print("%.3f" % spearman_result)

#To run main() function
if __name__ == "__main__":
    main()
