"""
Python 3 program to calculate an output using arithmetic operators

Task: Given the meal price (base cost of a meal), tip percent (the percentage
of the meal price being added as tip), and tax percent (the percentage of the 
meal price being added as tax) for a meal, find and print the meal's total cost.
Round the result to the nearest integer.

Input:
meal_cost = 12.00
tip_percent = 20
tax_percent = 8

Output:
total_cost = 15
"""
#Solve
def solve(meal_cost, tip_percent, tax_percent):
    #Initialization of variables
    total_cost = 0
    tip = 0
    tax = 0
    
    #Calculate tip
    tip = meal_cost * (tip_percent / 100)
    
    #Calculate tax
    tax = meal_cost * (tax_percent / 100)
    
    #Calculate total cost
    total_cost = meal_cost + tip + tax
    
    #Return total cost rounded off to the nearest integer
    return round(total_cost)

#Main
def main():
    #User input for meal cost
    meal_cost = float(input())
    
    #User input for tip percent
    tip_percent = int(input())
    
    #User input for tax percent
    tax_percent = int(input())
    
    #Calculate total cost
    total_cost = solve(meal_cost, tip_percent, tax_percent)
    
    #Print the output for total cost
    print(total_cost)
    
#To run main() function
if __name__ == "__main__":
    main()
