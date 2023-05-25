"""
Python 3 program to calculate Geometric Distribution

Task: The probability that a machine produces a defective product is 1/3.
What is the probability that the 1st defect occurs the 5th item produced?

Sample input: 
a = 1
b = 3
n = 5

Expected output:
Geometric Distribution: 0.066
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
    #User input for the inspection we want the probability of being the first defect for
    n = int(input())
    
    #Calculate Probability
    p = a / b
    
    #Calculate Geometric Distribution
    result = geometric(n, p)
    
    #Print the output for Geometric Distribution
    print("%.3f" % result)

#To run main() function
if __name__ == "__main__":
    main()
