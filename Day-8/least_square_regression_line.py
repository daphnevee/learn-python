"""
Python 3 program to calculate the Least Square Regression Line

Task: A group of five students enrolls in Statistics immediately after
taking a Math aptitude test. Each student's Math aptitude test score, x,
and Statistics course grade, y, can be expressed as the following list of
(x,y) points:
1. (95, 85)
2. (85, 95)
3. (80, 70)
4. (70, 65)
5. (60, 70)

Sample input: 
x1, y1 = 95 85
x2, y2 = 85 95
x3, y3 = 80 70
x4, y4 = 70 65
x5, y5 = 60 70

Expected output:
Value of y when x = 80: 78.288 
"""
#Import libraries
import math

#Mean
def mean(n, arr):
    return sum(arr) / n

#Least Square Regression Line
def regression(n, x, y):
    #Calculate the sum of data set x
    total_xi = sum(x)
    #Calculate the sum of data set y
    total_yi = sum(y)
    
    #Calculate the mean of data set x
    mean_xi = mean(n, x)
    #Calculate the mean of data set y
    mean_yi = mean(n, y)
    
    #Calculate the sum of x^2
    xi_squared = [xi ** 2 for xi in x]
    total_xi_squared = sum(xi_squared)
    
    #Calculate the sum of x*y
    xi_yi = list(map(lambda xi, yi: xi * yi, x, y))
    total_xi_yi = sum(xi_yi)
    
    #Calculate for the value of b
    b = ((n * total_xi_yi) - (total_xi * total_yi)) / (n * total_xi_squared - ((total_xi)**2))
    #Calculate for the value of a
    a = mean_yi - (b * mean_xi)
    
    return a, b

#Main
def main():
    #Hard-coded length of arrays x and y
    n = 5
    #User input for the elements of data sets x and y
    x = []
    y = []
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)
    
    #Calculate the equation of the best-fit line using the least squares method
    a, b = regression(n, x, y)
    
    #Calculate the value of y when x = 80 (y = a + bx)
    result = a + b*80
    
    #Print the output for y
    print("%.3f" % result)
    
#To run main() function
if __name__ == "__main__":
    main()
