"""
Python 3 program to calculate Geometric Distribution

Task: The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect is found during the first 5 inspections?

Sample input: 
a = 1
b = 3
n = 5

Expected output:
Geometric Distribution: 0.868
"""
#Geometric Distribution 
def geometric(n, p):
    #Probability of failure of 1 trial q
    q = 1 - p
    #Calculate Geometric Distribution
    geometric = q**(n - 1) * p 
    return geometric

#Main
def main():
    #User input for numerator & denominator for the probability of a defect
    a, b = list(map(float, input().split()))
    #User input for the inspection we want the probability of the first defect being discovered by
    n = int(input())
    
    #Calculate Probability
    p = a / b
    
    #Calculate Geometric Distribution
    result = 0
    for i in range(n + 1):
        if i > 0:
            result += geometric(i, p)
    #Print the output for Geometric Distribution
    print("%.3f" % result)

#To run main() function
if __name__ == "__main__":
    main()
