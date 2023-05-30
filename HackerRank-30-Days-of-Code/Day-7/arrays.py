"""
Python 3 program to utilize arrays

Task: Given an array, A, of N integers, print A's elements in reverse
order as a single line of space-separated numbers.

Input:
n = 4
a = 1 4 3 2

Output:
2 3 4 1

"""
#Main
def main():
    #User input for array size
    n = int(input())
    #Constraint: 1 <= N <= 1000
    if (n >= 1 and n <= 1000):
        #User input for array elements
        a = list(map(int, input().strip().split()))[:n]
        for i in range(n):
            #Constraint: 1 <= A[i] <= 10000
            if (a[i] >= 1 and a[i] <= 10000):
                #Reverse array elements using List Slicing
                reverse = a[::-1]
            else: 
                print("Elements should be within 1 to 10000")
        #Print reversed array as string
        print(' '.join(map(str, reverse)))
    else:
        print("Array size should be within 1 to 1000")
    
#To run main() function
if __name__ == "__main__":
    main()
