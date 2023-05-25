"""
Python 3 program to calculate Poisson Distribution

Task: A random variable, X, follows Poisson distribution with mean of 2.5.
Find the probability with which the random variable X is equal to 5.

Sample input: 
a = 2.5
k = 5

Expected output:
Geometric Distribution: 0.067
"""
#Factorial (Recursive approach)
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

#Poisson Distribution
def poisson(a, k, e):
    #Calculate Poisson Distribution
    poisson = (a**k * e**(-a)) / factorial(k)
    return poisson

#Main
def main():
    #User input for the mean of X
    a = float(input())
    
    #User input for the value we want the probability for
    k = int(input())
    
    #Hard-coded e value
    e = 2.71828
    
    #Calculate Poisson Distribution
    result = poisson(a, k, e)
    
    #Print the output for Poisson Distribution
    print("%.3f" % result)

#To run main() function
if __name__ == "__main__":
    main()
