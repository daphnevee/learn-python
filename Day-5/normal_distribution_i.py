"""
Python 3 program to calculate Normal Distribution

Task: In a certain plant, the time taken to assemble a car is a
random variable, X, having a normal distribution with a mean of
20 hours and a standard deviation of 2 hours. What is the probability
that a car can be assembled at this plant in:
1. Less than 19.5 hours?
2. Between 20 and 22 hours?

Sample input: 
mean = 20
std = 2
event_a = 19.5
event_b = 20 22

Expected output:
Probability for Event A: 0.401
Probability for Event B: 0.341
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
    #User input for the respective mean and standard deviation for X
    mean, std = list(map(float, input().split())) 
    
    #User input for Event A
    event_a = float(input()) 
    
    #User input for the respective lower & upper range boundaries for Event B
    event_b = list(map(float, input().split())) 
    
    #Event A: P(X < 19.5 hours)
    #Calculate Cumulative Probability for Event A
    result_a = cumulative_probability(event_a, mean, std)
    #Print the output for Event A
    print("%.3f" % result_a)
    
    #Event B: P(20 < X < 22)
    #Calculate Cumulative Probability for Event B
    result_b = cumulative_probability(event_b[1], mean, std) - cumulative_probability(event_b[0], mean, std)
    #Print the output for Event B
    print("%.3f" % result_b)

#To run main() function
if __name__ == "__main__":
    main()
