"""
Python 3 program to combine strings and loops

Task: Given a string, S, of length N that is indexed from 0 to N-1,
print its even-indexed and odd-indexed characters as 2 space-separated
strings on a single line.

Note: 0 is considered to be an even index.

Input:
t = 2
s = Hacker
s = Rank

Output:
s = Hacker -> Hce akr
s = Rank -> Rn ak

"""
#Main
def main():
    #User input for no. of test cases
    t = int(input())
    #Constraint: 1 <= T <= 10
    if (t >= 1 and t <= 10):
        for i in range(t):
            #User input for string
            s = str(input())
            #Initialize even & odd characters as string
            even = ''
            odd = ''
            #Constraint: 2 <= length of S <= 10000
            if (len(s) >= 2 and len(s) <= 10000):
                for j in range(len(s)):
                    #Get characters from even indices
                    if (j % 2):
                        even += s[j]
                    #Get characters from odd indices
                    else:
                        odd += s[j]    
                #Print output for odd characters and even characters of the string
                print("{} {}".format(odd, even))
            else:
                print("Length of string should only be between 2 and 10000")
    else:
        print("Number of test cases should only be between 1 and 10")
    
#To run main() function
if __name__ == "__main__":
    main()
