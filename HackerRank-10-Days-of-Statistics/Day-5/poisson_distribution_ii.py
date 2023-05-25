"""
Python 3 program to calculate Poisson Distribution

Task: The manager of an industrial plnt is planning to buy a machine
of either type A or type B. For each day's operation:
- The number of repairs, X, that machine A needs is a Poisson random
variable with mean 0.88. The daily cost of operating A is CA = 160 + 40X^2.
- The number of repairs, Y, that machine B needs is a Poisson random
variable with mean 1.55. The daily cost of operating B is CB = 128 + 40Y^2.

Assume that the repairs take a negligible amount of time and the machines
are maintained nightly to ensure that they operate like new at the start
of each day. Find and print the expected daily cost for each machine.

Sample input: 
a = 0.88
b = 1.55

Expected output:
Expected daily cost of Machine A: 226.176
Expected daily cost of Machine B: 286.100
"""
#Main    
def main():
    #User input for the respective means for A and B
    a, b = list(map(float, input().split()))
    
    #Calculate the expected daily cost of Machine A
    x = 160 + 40 * (a + a**2)
    #Print the output for Machine A
    print("%.3f" % x)
    
    #Calculate the expected daily cost of Machine B
    y = 128 + 40 * (b + b**2)
    #Print the output for Machine B
    print("%.3f" % y)

#To run main() function
if __name__ == "__main__":
    main()
