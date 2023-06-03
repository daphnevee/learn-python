"""
Python 3 program to utilize Abstract Classes

Task: Given a Book class and a Solution class, write a MyBook class
that does the following:
- Inherits from Book
- Has a parameterized constructor taking these 3 parameters:
    1. string title
    2. string author
    3. int price
- Implements the Book class' abstract display() method so it prints
these 3 lines:
    1. Title:, a space, and then the current instance's title
    2. Author:, a space, and then the current instance's author
    3. Price:, a space, and then the current instance's price

Note: Because these classes are being written in the same file,
you must not use an access modifier (e.g.: public) when declaring
MyBook or your code will not execute.

Input:
The Alchemist
Paulo Coelho
248

Output:
Title: The Alchemist
Author: Paulo Coelho
Price: 248

"""
#Import libraries
from abc import  ABCMeta, abstractmethod

#Book class (Base class)
class Book(object, metaclass=ABCMeta):
    #Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    #Abstract display() method
    @abstractmethod
    def display(): pass

#MyBook class (Derived class)
class MyBook(Book):
    #Constructor
    def __init__(self, title, author, price):
        #Inherit all methods & properties from parent class
        super().__init__(title, author)
        #Add property for price
        self.price = price
    
    #Display method to print book details
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Price:", self.price)

#Main
def main():
    #User input for book title
    title = str(input())
    #User input for author's name
    author = str(input())
    #User input for book price
    price = int(input())
    
    #Instance object of MyBook class
    new_novel = MyBook(title, author, price)
    
    #Calling display() method of MyBook class
    new_novel.display()
    
#To run main() function
if __name__ == "__main__":
    main()