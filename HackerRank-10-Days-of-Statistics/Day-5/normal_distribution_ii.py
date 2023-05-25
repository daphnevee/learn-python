"""
Python 3 program to calculate Normal Distribution

Task: The final grades for a Physics exam taken by a large group
of students have a mean of μ = 70 and a standard deviation of σ = 10.
If we can approximate the distribution of these grades by a normal
distribution, what percentage of the students:
1. Scored higher than 80 (i.e., have a grade > 80)?
2. Passed the test (i.e., have a grade >= 60)?
3. Failed the test (i.e., have a grade < 60)?

Find and print the answer to each question on a new line, rounded to
a scale of 2 decimal places.

Sample input: 
mean = 70
std = 10
high_score = 80
passing_score = 60

Expected output:
Probability for Event A: 15.87
Probability for Event B: 84.13
Probability for Event C: 15.87
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
    #User input for the respective mean & standard deviation for the exam
    mean, std = list(map(float, input().split()))
    
    #User input for Event A
    high_score = float(input()) 
    
    #User input for Events B & C
    passing_score = float(input())
    
    #Event A: Scored higher than 80 (grade > 80)
    #Calculate Cumulative Probability for Event A
    event_a = cumulative_probability(high_score, mean, std)
    #Percentage of students that have a high score
    result_a = 100 - (event_a * 100)
    #Print the output for Event A
    print("%.2f" % result_a)
    
    #Event B: Passed the test (grade >= 60)
    event_b = cumulative_probability(passing_score, mean, std)
    #Percentage of students that passed the test
    result_b = 100 - (event_b * 100)
    #Print the output for Event B
    print("%.2f" % result_b)
    
    #Event C: Failed the test (grade < 60)
    event_c = cumulative_probability(passing_score, mean, std)
    #Percentage of students that failed the test
    result_c = event_c * 100
    #Print the output for Event C
    print("%.2f" % result_c)

#To run main() function
if __name__ == "__main__":
    main()
