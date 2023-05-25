"""
Python 3 program to calculate a problem based on the Central Limit Theorem

Task: The number of tickets purchased by each student for the University X vs. University Y football
game follows a distribution that has a mean of μ = 2.4 and a standard deviation of σ = 2.0.

A few hours before the game starts, 100 eager students line up to purchase last-minute tickets.
If there are only 250 tickets left, what is the probability that all 100 students will be able
to purchase tickets?

Sample input: 
total_tickets = 250
n = 100
mean = 2.4
std = 2.0

Expected output:
Probability for Event: 0.6915
"""
#Import libraries
import math

#Cumulative Probability
def cumulative_probability(x, mean, std):
    #Calculate Cumulative Probability
    cumulative_probability = (1/2) * (1 + math.erf((x - mean)/(std * math.sqrt(2))))
    return cumulative_probability

#Main
def main():
    #User input for the no. of last-minute tickets available at the box office
    total_tickets = float(input())
    
    #User input for the no. of students waiting to buy tickets
    n = float(input())
    
    #User input for the mean no. of purchased tickets
    mean = float(input())
    
    #User input for the standard deviation
    std = float(input())
    
    #Calculate μ'
    mean2 = n * mean
    
    #Calculate σ'
    std2 = math.sqrt(n) * std
    
    #Calculate Cumulative Probability
    result = cumulative_probability(total_tickets, mean2, std2)
    
    #Print the output for the Cumulative Probability of the event
    print("%.4f" % result)

#To run main() function
if __name__ == "__main__":
    main()
