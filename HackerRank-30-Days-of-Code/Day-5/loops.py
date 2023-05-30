"""
Python 3 program to use loops

Task: Given an integer, n, print its first 10 multiples. Each multiple 
n x i (where 1 <= i <= 10) should be printed on a new line in the form:
n x i = result.

Input:
n = 2

Output:
2 x 1 = 2
2 x 2 = 4
2 x 3 = 6
2 x 4 = 8
2 x 5 = 10
2 x 6 = 12
2 x 7 = 14
2 x 8 = 16
2 x 9 = 18
2 x 10 = 20

"""
#Main
def main():
    #User input for single integer, n
    n = int(input())
    #Constraint: 2 <= n <= 20
    if (n >= 2 and n <= 20):
        #Calculate first 10 multiples
        #Constraint: 1 <= i <= 10
        for i in range(1, 11):
            result = n * i
            print("%d x %d = %d" % (n, i, result))
    else:
        print("Input numbers only from 2 to 20")
    
#To run main() function
if __name__ == "__main__":
    main()
