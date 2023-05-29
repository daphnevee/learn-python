"""
Python 3 program to calculate an output using conditional statements

Task: Given an integer, n, perform the ff. conditional actions:
- If n is odd, print Weird
- If n is even and in the inclusive range of 2 to 5, print Not Weird
- If n is even and in the inclusive range of 6 to 20, print Weird
- If n is even and greater than 20, print Not Weird

Input:
n = 3
n = 24 

Output:
Weird
Not Weird

"""
#User input for integer
n = int(input())
#Constraint: 1 <= n <= 100 (positive integers only)
if n not in range(1, 101):
    print("Integers within 1 to 100 are only allowed")
else:
    #Condition 1: Integer is even
    if (n % 2) == 0:
        #Condition 1a: Integer is even & within range of 2 to 5
        if n in range(2, 6):
            print("Not Weird")
        #Condition 1b: Integer is even & within range of 6 to 20
        elif n in range(6, 21):
            print("Weird")
        #Condition 1c: Integer is even & greater than 20
        else:
            print("Not Weird")
    #Condition 2: Integer is odd
    else:
        print("Weird")
