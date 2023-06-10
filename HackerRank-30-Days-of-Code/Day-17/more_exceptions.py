"""
Python 3 program to manage exceptional situations by using try and catch blocks

Task: Write a Calculator class with a single method: int power(int, int).
The power method takes two integers, n and p, as parameters and returns
the integer result of n^p. If either n or p is negative, then the method
must throw an exception with the message: "n and p should be non-negative".

Note: Do not use an access modifier (e.g.: public) in the declaration for
your Calculator class.

Input:
T = 4
T0: n = 3, p = 5
T1: n = 2, p = 4
T2: n = -1, p = -2
T3: n = -1, p = 3

Output:
T0: 243
T1: 16
T2: n and p should be non-negative
T3: n and p should be non-negative

"""
#Calculator class
class Calculator:
    #Power method
    def power(self, n, p):
        if (n < 0 or p < 0):
            #Throw exception when n or p are negative
            raise Exception("n and p should be non-negative")
        else:
            #Calculate power
            power = (n ** p)
        
        return power

#Main
def main():
    #User input for no. of test cases
    T = int(input())
    #Instance object of Calculator class
    myCalculator = Calculator()
    for i in range(T):
        #User input for n and p 
        n, p = map(int, input().split())
        try:
            #Calculate power
            ans = myCalculator.power(n, p)
            #Print power output
            print(ans)
        #Handles raised exception
        except Exception as e:
            print(e)
        
#To run main() function
if __name__ == "__main__":
    main()