"""
Python 3 program to parse an integer from a string and print a custom error message

Task: Read a string, S, and print its integer value; if S cannot be converted to
an integer, print "Bad String."

Input:
S1 = 3
S2 = za

Output:
S1: 3
S2: Bad string

"""

#Main
def main():
    #User input for string
    S = input()
    try:
        #Print the parsed integer value of S
        print(int(S))
    except ValueError:
        print("Bad String")
        
#To run main() function
if __name__ == "__main__":
    main()