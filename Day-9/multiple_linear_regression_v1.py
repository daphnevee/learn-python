"""
Python 3 program to calculate Multiple Linear Regression (Version 1)

Task: Andrea has a simple equation: Y = a + b1 * f1 + b1 * f2 + ... + bm * fm
for (m + 1) real constants (a, f1, f2, ..., fm). We can say that the value of Y
depends on m features. Andrea studies this equation for n different feature sets
(f1, f2, f3,..., fm) and records each respective value of Y. If she has q new
feature sets, can you help Andrea find the value of Y for each of the sets?

Note: You are not expected to account for bias and variance trade-offs.

Sample input: 
m = 2
n = 7
values:
0.18 0.89 109.85
1.0 0.26 155.72
0.92 0.11 137.66
0.07 0.37 76.17
0.85 0.16 139.75
0.99 0.41 162.6
0.87 0.47 151.77
q = 4
values:
0.49 0.18
0.57 0.83
0.56 0.64
0.76 0.18

Expected output:
Value for Y1 for q1 feature set: 105.22
Value for Y2 for q2 feature set: 142.68
Value for Y3 for q3 feature set: 132.94
Value for Y4 for q4 feature set: 129.71
"""
#Import libraries
from sklearn import linear_model
import numpy as np

#Calculate the Multiple Linear Regression
def multiple_linear_regression(x, y):
    #Set the model LinearRegression using sklearn's built-in library
    lm = linear_model.LinearRegression()
    lm.fit(x, y)
    #Calculate for the value of a
    a = lm.intercept_
    #Calculate for the value of b
    b = lm.coef_
    return a, b

#Main
def main():
    #User input for m (the no. of observed features) & n (the no. of feature sets Andrea studied)
    m, n = list(map(int, input().split()))
    
    #User input for the m observed features and the Y feature set
    values = [list(float(x) for x in input().split()) for i in range(n)]
    
    #Get m observed features and store in x
    x = np.array([[value[i] for i in range(m)] for value in values])
    
    #Get y feature set values and store in y
    y = np.array([value[-1] for value in values])
    
    #Calculate Multiple Linear Regression
    a, b = multiple_linear_regression(x,y)
    
    #User input for the no. of feature sets Andrea wants to query for
    q = int(input())
    
    #User input for the q feature sets
    for i in range(q):
        values = list(map(float, input().split()))
        #Predict y 
        #a) y_hat = beta * X
        result = [b[j] * values[j] for j in range(m)]
        #b) y = f(x) = beta_0 + beta_1 * X_1 + beta_2 * X_2 + ... + beta_k * x_k + err
        result = a + np.sum(result)
        #Print the values of Y for each of the q feature sets
        print("%.3f" % result)

#To run main() function
if __name__ == "__main__":
    main()
