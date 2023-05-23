"""
Python 3 program to calculate Quartiles

Task: Given an array, arr, of n integers, calculate the respective
first quartile (Q1), second quartile (Q2), and third quartile (Q3).
It is guaranteed that Q1, Q2, and Q3 are integers.

Sample input: 
n = 9
arr = 3 7 8 5 12 14 21 13 18

Expected output:
Q1 = 6
Q2 = 12
Q3 = 16

"""

#Median 
def median(arr):
    n = len(arr)
    
    #Case 1: Even no. of elements
    if n % 2 == 0: #even
        return (arr[n//2] + arr[n//2 - 1])/2
    
    #Case 2: Odd no. of elements
    return arr[n//2] #odd

#Lower Quartile
def lower_quartile(n, arr):
    return median(arr[:n//2]) 

#Upper Quartile
def upper_quartile(n, arr):
    #Case 1: Odd no. of elements
    if n % 2 == 1: 
        return median(arr[n//2+1:])
    
    #Case 2: Even no. of elements
    return median(arr[n//2:]) 
            
#Main 
def main():
    #User input for the length of the array
    n = int(input())
    
    #User input for the elements of the array
    arr = list(map(int, input().strip().split()))[:n]
    
    #Sort the elements in the array
    arr.sort()
    
    #Calculate the Quartiles
    median_result = median(arr)
    lower_quartile_result = lower_quartile(n, arr)
    upper_quartile_result = upper_quartile(n, arr)
    
    #Print the output for Q1, Q2, Q3
    print(int(lower_quartile_result))
    print(int(median_result))
    print(int(upper_quartile_result))
    
#To run main() function
if __name__ == "__main__":
    main()
