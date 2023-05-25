"""
Python 3 program to calculate Binomial Distribution

Task: A manufacturer of metal pistons finds that, on average, 12% of
the pistons they manufacture are rejected because they are incorrectly
sized. What is the probability that a batch of 10 pistons will contain:
1. No more than 2 rejects?
2. At least 2 rejects?

Sample input: 
p = 12
n = 10

Expected output:
Binomial Distribution for Condition A: 0.891
Binomial Distribution for Condition B: 0.342
"""
#Factorial (Recursive approach)
def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n - 1)

#Binomial
def binomial(x, n, p):
    #Probability of failure of 1 trial q
    q = 1 - p
    #Calculate nCr
    nCr = factorial(n) / (factorial(x) * factorial(n - x))
    #Calculate binomial probability
    binomial = nCr * (p**x) * q**(n - x)
    return binomial

#Main
def main():
    #User input for the respective percentage of defective pistons (p) 
    #and the size of the current batch of pistons (n)
    p, n = list(map(float, input().split())) 
    
    #Convert percentage to decimal
    p = p / 100
    
    #Condition A: No more than 2 rejects (x <= 2)
    a = 0
    #Calculate Binomial Distribution
    for x in range(int(n)):
        if x <= 2:
            a += binomial(x, n, p)
    #Print the output for Binomial Distribution of Condition A
    print("%.3f" % a)

    #Condition B: At least 2 rejects (x >= 2)
    b = 0
    #Calculate Binomial Distribution
    for x in range(int(n)):
        if x >= 2:
            b += binomial(x, n, p)
    #Print the output for Binomial Distribution of Condition B
    print("%.3f" % b)

#To run main() function
if __name__ == "__main__":
    main()
