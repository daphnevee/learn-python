"""
Python 3 program to demonstrate Classes and Instances (Object-Oriented Programming)

Task: Write a Person class with an instance variable, age, and a constructor that
takes an integer, initialAge, as a parameter. The constructor must assign initialAge
to age after confirming the argument passed as initialAge is not negative; if a 
negative argument is passed as initialAge, the constructor should set age to 0 and
print "Age is not valid, setting age to 0." In addition, you must write the following
instance methods:
1. yearPasses() should increase the age instance variable by 1.
2. amIOld() should perform the following conditional actions:
- If age < 13, print "You are young."
- If age >= 13 and age < 18, print "You are a teenager."
- Otherwise, print "You are old."

Input:
t = 4
Test Case 0: age = -1
Test Case 1: age = 10
Test Case 2: age = 16
Test Case 3: age = 18

Output:
Test Case 0: age = -1 -> Age is not valid, setting age to 0.
age = 0 -> You are young.
age = 3 -> You are young.

Test Case 1: age = 10
age = 10 -> You are young.
age = 13 -> You are a teenager.

Test Case 2: age = 16
age = 16 -> You are a teenager.
age = 19 -> You are old.

Test Case 3: age = 18
age = 18 -> You are old.
age = 21 -> You are old.

"""
#Person Class
class Person:
    #Constructor with parameter "initialAge"
    def __init__(self, initialAge):
        #Check if initialAge is negative
        if (initialAge < 0):
            print("Age is not valid, setting age to 0.")
            #Set age to 0
            self.age = 0
        else:
            #Set user input initialAge as age
            self.age = initialAge
    
    #Check if person is of old age
    def amIOld(self):
        #Condition A: Age < 13
        if (self.age < 13):
            print("You are young.")
        #Condition B: 13 <= Age < 18
        elif (self.age >= 13 and self.age < 18):
            print("You are a teenager.")
        #Condition C: Age >= 18
        else: 
            print("You are old.")
            
    #Age increases as another year passes
    def yearPasses(self):
        self.age += 1
        
#User input for the no. of test cases
t = int(input())

#Constraint: 1 <= T <= 4
for i in range(0, t):
    #User input for Age
    age = int(input())
    #Constraint: -5 <= age <= 30
    if age in range(-5, 31):
        #Instance variable, age
        p = Person(age)
        #Check if person is of old age
        p.amIOld()
        #Age increases as years pass
        #Constraint: Increase only by 3 (based on Test Cases)
        for j in range(0, 3):
            p.yearPasses()
        #Check if person is of old age after years pass
        p.amIOld()
        print("")
    else:
        print("Age should only be between -5 and 30")
