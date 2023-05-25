"""
Python 3 program to calculate a problem based on the Central Limit Theorem

Task: A large elevator can transport a maximum of 9800 pounds. Suppose a load
of cargo containing 49 boxes must be transported via the elevator. The box weight
of this type of cargo follows a distribution with a mean of μ = 205 pounds
and a standard deviation of σ = 15 pounds. 

Based on this information, what is the probability that all 49 boxes can be safely
loaded into the freight elevator and transported?

Sample input: 
max_weight = 9800
n = 49
mean = 205
std = 15

Expected output:
Probability for Event: 0.0098
"""

#Importing libraries
import math

#Cumulative Probability
def cumulative_probability(x, mean, std):
    #Calculate Cumulative Probability
    cumulative_probability = (1/2) * (1 + math.erf((x - mean)/(std * math.sqrt(2))))
    return cumulative_probability

#Main
def main():
    #User input for the maximum weight the elevator can transport
    max_weight = float(input())
    
    #User input for the no. of boxes in the cargo
    n = float(input())
    
    #User input for the mean weight of a cargo box
    mean = float(input())
    
    #User input for the standard deviation
    std = float(input())
    
    #Calculate μ'
    mean2 = n * mean
    
    #Calculate σ'
    std2 = math.sqrt(n) * std
    
    #Calculate Cumulative Probability
    result = cumulative_probability(max_weight, mean2, std2)
    
    #Print the output for the Cumulative Probability of the event
    print("%.4f" % result)

#To run main() function
if __name__ == "__main__":
    main()
