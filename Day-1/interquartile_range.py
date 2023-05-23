"""
Python 3 program to calculate Interquartile Range

Task: The interquartile range of an array is the difference between its
first (Q1) and third (Q3) quartiles (i.e., Q3 - Q1).

Given an array, values, of n integers and an array, freqs, representing
the respective frequencies of values' elements, construct a data set, S,
where each values[i] occurs at frequency freqs[i]. Then calculate and print
S's interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).

Tip: Be careful to not use integer division when averaging the middle of two
elements for a data set with an even number of elements, and be sure to not
include the median in your upper and lower data sets.

Sample input: 
n = 6
values = 6 12 8 10 20 16
freqs = 5 4 3 2 1 5

Expected output:
Interquartile Range: 9.0
"""

#Median 
def median(arr):
    n = len(arr)
    
    #Case 1: Even no. of elements
    if n % 2 == 0: 
        return (arr[n//2] + arr[n//2 - 1])/2
    
    #Case 2: Odd no. of elements
    return arr[n//2] 

#Lower Quartile
def lower_quartile(n, S):
    return median(S[:n//2])

#Upper Quartile
def upper_quartile(n, S):
    #Case 1: Odd no. of elements
    if n % 2 == 1: 
        return median(S[n//2+1:]) 
    
    #Case 2: Even no. of elements
    return median(S[n//2:])

#Interquartile Range
def interquartile_range(n, S):
    q1 = lower_quartile(n, S)
    q3 = upper_quartile(n, S)
    interquartile_range = q3 - q1
    
    return interquartile_range
            
#Main Function
def main():
    #User input for the length of both arrays
    n = int(input())
    
    #User input for the elements of values[] array
    values = list(map(int, input().strip().split()))[:n]
    
    #User input for the elements of freqs[] array
    freqs = list(map(int, input().strip().split()))[:n]
    
    #Apply the frequencies to the values to get the expanded array
    S = []
    for i in range(n): 
        for j in range(freqs[i]):
            S.append(values[i]) 
    #Sort the expanded array
    S.sort()
    #Get the length of the expanded array to calculate the quartiles
    n = len(S)

    #Calculate the Interquartile Range
    interquartile_range_result = interquartile_range(n, S)
    
    #Print the output for the Interquartile Range
    print("%.1f" % interquartile_range_result)
    
#To run main() function
if __name__ == "__main__":
    main()
