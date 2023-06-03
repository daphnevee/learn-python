"""
Python 3 program to demonstrate Inheritance

Task: You are given two classes, Person and Student, where Person
is the base class and Student is the derived class. Completed code
for Person and a declaration for Student are provided for you in
the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:
- A Student class constructor, which has 4 parameters:
    1. A string, firstName
    2. A string, lastName
    3. An integer, idNumber
    4. An integer array (or vector) of test scores, scores
- A char calculate() method that calculates a Student object's average
and returns the grade character representative of their calculated average.

Grading Scale
Letter - Average(a)
O - 90 <= a <= 100
E - 80 <= a < 90
A - 70 <= a < 80
P - 55 <= a < 70
D - 40 <= a < 55
T - a < 40

Input:
firstName, lastName, idNumber = Heraldo Memelli 8135627
n_test_scores = 2
scores = 100 80

Output:
Name: Memelli, Heraldo
ID: 8135627
Grade: O
"""
#Person class (Base class)
class Person:
    #Constructor with parameters firstName, lastName, idNumber
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        
    #Print person's details
    def printPerson(self):
        print("Name:", self.lastName + ", " + self.firstName)
        print("ID: " + self.idNumber)
        
#Student class (Derived class)
class Student(Person):
    #Constructor with parameters firstName, lastName, idNumber, scores
    def __init__(self, firstName, lastName, idNumber, scores):
        #Inherit all methods & properties from parent class
        super().__init__(firstName, lastName, idNumber)
        #Add property for scores
        self.scores = scores
        
    #Calculate grade based on scores
    def calculate(self):
        #Get average of scores
        a = sum(self.scores)/len(self.scores)
        #Check calculated grade based on average score
        if (a >= 90 and a <= 100):
            return "O"
        elif (a >= 80 and a < 90):
            return "E"
        elif (a >= 70 and a < 80):
            return "A"
        elif (a >= 55 and a < 70):
            return "P"
        elif (a >= 40 and a < 55):
            return "D"
        else:
            return "T"

#Main
def main():
    #User input for Student information
    firstName, lastName, idNumber = list(map(str, input().split()))
    #Constraint: 1 <= length of firstName, length of lastName <= 10
    #Constraint: length of idNumber = 7
    if ((1 >= len(firstName) <= 10) or (1 >= len(lastName) <= 10) or (len(idNumber) == 7)):
        #User input for no. of test scores
        n_test_scores = int(input())
        #User input for test scores
        scores = list(map(int, input().split()))
        #Instance variable of Student's firstName, lastName, idNumber, scores
        s = Student(firstName, lastName, idNumber, scores)
    
        #Print person's details of firstName, lastName, idNumber
        s.printPerson()
        
        #Iterate through scores
        for i in range(n_test_scores):
            #Constraint: 0 <= score <= 100
            if (scores[i] >= 0 and scores[i] <= 100):
                #Print student's calculated grade based on scores
                final_grade = s.calculate()
            else:
                print("Scores should only be between 0 and 100")
        #Print the output for the student's calculated grade
        print("Grade:", s.calculate())
        
    else:
        print("Length of first name and last name must be between 1 and 10. Length of ID number must only be 7.")
    
#To run main() function
if __name__ == "__main__":
    main()