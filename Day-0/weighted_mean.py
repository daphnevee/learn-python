"""
Python 3 program to calculate Weighted Mean

Task: Given an array, X, of N integers and an array, W, representing
the respective weights of X's elements, calculate and print the weighted
mean of X's elements. Your answer should be rounded to a scale of 1 
decimal place (i.e., 12.3 format)

Sample input: 
n = 5
X[] = 10 40 30 50 20
W[] = 1 2 3 4 5

Expected output:
Weighted Mean: 32.0
"""

#Weighted Mean
def weightedMean(n, X, W):
    sum_product = 0
    total_weights = 0
    for i in range(n):
        #Multiply each element in X[] with the corresponding weight in W[] and sum them
        sum_product += X[i] * W[i]
        #Sum of weights in W[]
        total_weights += W[i]
    
    #Calculate weighted mean 
    weighted_mean = sum_product / total_weights
    
    return weighted_mean
            
#Main
def main():
    #User input for the length of both X[] and W[] arrays
    n = int(input())
    
    #User input for the elements of X[] array
    X = list(map(int, input().strip().split()))[:n]
    
    #User input for the elements of W[] array
    W = list(map(int, input().strip().split()))[:n]
    
    #Calculate the Weighted Mean of the elements
    weighted_mean_result = weightedMean(n, X, W)
    
    #Print the output for the Weighted Mean
    print("%.1f" % weighted_mean_result)
    

#To run main() function
if __name__ == "__main__":
    main()
