"""
Python 3 program to calculate Spearman's Rank Correlation Coefficient (Version 1)

Task: Given two n-element data sets, X and Y, calculate the value of
Spearman's rank correlation coefficient.

Sample input: 
n = 10
x = 10 9.8 8 7.8 7.7 1.7 6 5 1.4 2
y = 200 44 32 24 22 17 15 12 8 4

Expected output:
Spearman's Rank Correlation Coefficient: 0.903
"""
#Import libraries
import math

#Rank
def rank(arr):
    arr = [sorted(arr).index(i) for i in arr]
    return arr

#Spearman's Rank Correlation Coefficient
def spearman(n, p, q):  
    #Sum of the difference bet. the respective values of Rank X & Rank Y
    di = 0
    for i in range(n):
        di += (p[i] - q[i])**2
    
    #Calculate Spearman's Rank Correlation Coefficient
    spearman = 1 - ((6 * di)/(n*(n**2 - 1)))
    
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
    p = rank(x)
    
    #Rank the elements of data set Y
    q = rank(y)
        
    #Calculate Spearman's Rank Correlation Coefficient for data set X and Y
    spearman_result = spearman(n, p, q)
    
    #Print the output for Spearman's Rank Correlation Coefficient
    print("%.3f" % spearman_result)

#To run main() function
if __name__ == "__main__":
    main()
