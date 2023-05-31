"""
Python 3 program using Recursion

Task: Calculate Factorial using Recursive Method

Input:
n = 3

Output:
factorial_result = 6

"""
#Factorial (Recursive Method)
def factorial(n):
    #Base Case
    if (n <= 1):
        return 1
    #Recursive
    else:
        return n * factorial(n-1)

#Main
def main():
    #User input for integer
    n = int(input())
    #Constraint: 2 <= n <= 12
    if (n >= 2 and n <= 12):
        #Calculate Factorial
        factorial_result = factorial(n)
        #Print output for Factorial
        print(factorial_result)
    else:
        print("Input must be between 2 and 12.")
    
#To run main() function
if __name__ == "__main__":
    main()
