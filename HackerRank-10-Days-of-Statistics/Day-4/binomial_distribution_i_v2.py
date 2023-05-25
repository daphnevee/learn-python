"""
Python 3 program to calculate Binomial Distribution I (Version 2)

Task: The ratio of boys to girls for babies born in Russian is 1.09 : 1.
If there is 1 child born per bith, what proportion of Russian families
with exactly 6 children will have at least 3 boys?

Write a program to compute the answer using the above parameters.
Then print your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).

Sample input: 
a = 1.09
b = 1

Expected output:
Binomial Distribution: 0.696
"""
#Import libraries
import math

#Binomial 
def binomial(x, n, p):
    #Probability of failure of 1 trial q
    q = 1 - p
    #Calculate nCr
    nCr = math.factorial(n) / (math.factorial(x) * math.factorial(n - x))
    #Calculate binomial probability
    binomial = nCr * (p**x) * q**(n - x)
    return binomial

#Main
def main():
    #User input for ratio of boys to girls for babies born in Russia
    a, b = list(map(float, input().split()))
    #Hard-coded total no. of trials
    n = 6
    
    #Calculate Probability
    p = a / (a + b)
    
    #Calculate Binomial Distribution
    result = binomial(3, n, p) + binomial(4, n, p) + binomial(5, n, p) + binomial(6, n, p)
    
    #Print the output for Binomial Distribution 
    print("%.3f" % result)

#To run main() function
if __name__ == "__main__":
    main()
