"""
Python 3 program to demonstrate Scope

Task: Complete the Difference class by writing the ff:
- A class constructor that takes an array of integers as a parameter
and saves it to the __elements instance variable.
- A computeDifference method that finds the maximum absolute
difference between any 2 numbers in __elements and stores it
in the maximumDifference instance variable.

Input:
STDIN  Function 
-----  --------
3      __elements[] size N = 3
1 2 5  __elements = [1, 2, 5]

Output:
4

"""
#Difference class
class Difference:
    #Constructor
    def __init__(self, a):
        self.__elements = a
    
    #Compute Absolute Difference Method
    def computeDifference(self):
        #Store elements in variable arr
        arr = self.__elements
        #Initialization of maximumDifference variable
        maximumDifference = 0
        #Iterate through elements
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                #Calculate absolute difference
                absoluteDifference = abs(arr[j] - arr[i])
                #Check if current absolute difference is maximum difference
                if (absoluteDifference > maximumDifference):
                    maximumDifference = absoluteDifference
        
        self.maximumDifference = maximumDifference

#Main
def main():
    #User input for array size
    _ = input()
    #User input for elements
    a = [int(e) for e in input().split(' ')]
    
    #Instance object of Difference class
    d = Difference(a)
    #Calculate absolute difference between elements
    d.computeDifference()
    
    #Print the output for maximum absolute difference
    print(d.maximumDifference)
    
#To run main() function
if __name__ == "__main__":
    main()