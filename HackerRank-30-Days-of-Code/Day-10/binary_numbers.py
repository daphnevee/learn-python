"""
Python 3 program to calculate Binary Numbers

Task: Given a base-10 integer, n, convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum
number of consecutive 1's in n's binary representation. When working
with different bases, it is common to show the base as a subscript.

Input:
n = 5
n = 13

Output:
max_result = 1
max_result = 2

"""
#Convert Decimal to Binary
def decimal_to_binary(n):
    #Create list to store binary
    remainders = []
    while (n > 0):
        #Calculate remainder of decimal
        remainder = n % 2
        #Divide decimal by 2 (Floor division)
        n = n // 2
        #Add remainder to list
        remainders.append(remainder)
    return remainders

#Count maximum no. of consecutive 1s in binary representation of 1
def maxConsecutive1s(remainders):
    #Initialization of variables
    count = 0
    max_count = 0
    #Iterate through binary
    for i in range(len(remainders)):
        #Check if binary is 1
        if remainders[i] == 1:
            #Increment counter
            count += 1
            #Check if max count has been reached
            if (count > max_count):
                max_count = count
        else:
            count = 0
    return max_count

#Main
def main():
    #User input for integer
    n = int(input())
    #Constraint: 1 <= n <= 10^6
    if (n >= 1 and n <= 1000001):
        #Convert decimal to binary
        conversion_result = decimal_to_binary(n)
        #Calculate max no. of consecutive 1s in binary representation of n
        max_result = maxConsecutive1s(conversion_result)
        #Print the output
        print(max_result)
    else:
        print("Integer must be between 1 to 1000000")
    
#To run main() function
if __name__ == "__main__":
    main()
