"""
Python 3 program to calculate a problem based on the Central Limit Theorem

Task: You have a sample of 100 values from a population with mean μ = 500
and with standard deviation σ = 80. Compute the interval that covers the 
middle 95% of the distribution of the sample mean; in other words, compute
A and B such that P(A < x < B) = 0.95. Use the value of z = 1.96.
Note that z is the z-score.

Sample input: 
s = 100
mean = 500
std = 80
p = .95
z = 1.96

Expected output:
A: 484.32
B: 515.68
"""
#Import libraries
import math

#Main
def main():
    #User input for the sample size
    s = float(input()) 
    
    #User input for the mean
    mean = float(input()) 
    
    #User input for the standard deviation
    std = float(input())
    
    #User input for the distribution percentage (in decimal)
    p = float(input()) 
    
    #User input for the value of z-score
    z = float(input()) 
    
    #Calculate μ'
    mean2 = s * mean
    #Calculate σ'
    std2 = math.sqrt(s) * std

    #Calculate for the value of A
    A = (mean2 - std2 * z)/s
    #Print the output for A
    print("%.2f" % A)
    
    #Calculate for the value of B
    B = (mean2 + std2 * z)/s
    #Print the output for B
    print("%.2f" % B)

#To run main() function
if __name__ == "__main__":
    main()
