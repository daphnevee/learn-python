"""
Python 3 program to utilize 2D Arrays

Task: Calculate the hourglass sum for every hourglass in A,
then print the maximum hourglass sum.

Input:
A = 1 1 1 0 0 0
    0 1 0 0 0 0
    1 1 1 0 0 0
    0 0 2 4 4 0
    0 0 0 2 0 0
    0 0 1 2 4 0

Output:
max_sum_result = 19
"""

def MaxHourglassSum(R, C, A):
    #Negative values
    max_sum = -50000
    #Positive values
    #max_sum = 0
    
    #Condition: Hourglass must have 3 rows & columns
    if(R < 3 or C < 3):
        print("Max hourglass sum cannot be computed.")
    
    #Calculate max sum of hourglass
    for i in range(0, R-2):
        for j in range(0, C-2):
            current_sum = (A[i][j] + A[i][j + 1] + A[i][j + 2] + A[i + 1][j + 1] +
                      A[i + 2][j] + A[i + 2][j + 1] + A[i + 2][j + 2])
            
            if (current_sum > max_sum):
                max_sum = current_sum
            
    return max_sum

#Main
def main():
    #Create 2D array
    A = []
    #Hard-coded 6x6 matrix
    n_rows = 6
    n_cols = 6
    #User input for array elements
    for i in range(n_rows):
        #User input for row elements
        row = list(map(int, input().split()))
        #Append row to A 
        A.append(row)
    
    #Calculate maximum hourglass sum
    max_sum_result = MaxHourglassSum(n_rows, n_cols, A)
    #Print the output for maximum hourglass sum
    print(max_sum_result)
    
#To run main() function
if __name__ == "__main__":
    main()
