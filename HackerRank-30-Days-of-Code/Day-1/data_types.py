"""
Python 3 program to print data types

Task: Complete the code in the editor below. The variables i, d, and s are already
declared and initialized for you. You must:
1. Declare 3 variables: one of type int, one of type double, and one of type String.
2. Read 3 lines of input from stdin (according to the sequence given in the Input Format
section below) and initialize your 3 variables.
3. Use the + operator to perform the ff. operations:
    1) Print the sum of i plus your int variable on a new line.
    2) Print the sum of d plus your double variable to a scale of one decimal place on a new line.
    3) Concatenate s with the string you read as input and print the result on a new line.
    
Note: If you are using a language that doesn't support using + for string concatenation (e.g.: C),
you can just print  one variable immediately following the other on the same line. The string 
provided in your editor must be printed first, immediately followed by the string you read as input.

Input:
j = 12
e = 4.0
a = is the best place to learn and practice coding!

Output:
sum_of_integers: 16
sum_of_floats: 8.0
concat_strings: HackerRank is the best place to learn and practice coding!
"""
#Hard-coded integer, double, string
i = 4
d = 4.0
s = 'HackerRank '

#User input for integer
j = int(input())

#User input for double
e = float(input())

#User input for string
a = str(input())

#Calculate sum of integers
sum_of_integers = i + j
#Print output for sum of integers
print(sum_of_integers)

#Calculate sum of floats
sum_of_floats = d + e
#Print the output for sum of floats
print(sum_of_floats)

#Concatenate strings
concat_strings = s + a
#Print the output for concatenated strings
print(concat_strings)
