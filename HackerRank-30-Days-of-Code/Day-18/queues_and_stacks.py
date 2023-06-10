"""
Python 3 program to utilize Stacks and Queues

Task: A palindrome is a word, phrase, number, or other sequence of
characters which reads the same backwards and forwards. Can you
determine if a given string, s, is a palindrome?

To solve this challenge, we must first take each character in s,
enqueue it in a queue, and also push that same character onto a 
stack. Once that's done, we must dequeue the first character from
the queue and pop the top character off the stack, then compare
the two characters to see if they are the same; as long as the
characters match, we continue dequeueing, popping, and comparing
each character until our containers are empty (a non-match means
s isn't a palindrome).

Write the ff. declarations and implementations:
1. Two instance variables: one for your stack, and one for your queue.
2. A void pushCharacter(char ch) method that pushes a character onto a stack.
3. A void enqueueCharacter(char ch) method that enqueues a character
in a queue instance variable.
4. A char popCharacter() method that pops and returns the character
at the top of the stack instance variable.
5. A char dequeueCharacter() method that dequeues and returns the first
character in the queue instance variable.

Input:
s = racecar

Output:
The word, racecar, is a palindrome.

"""
#Solution class
class Solution:
    #Constructor
    def __init__(self):
        #Instance variable for stack
        self.stack = []
        #Instance variable for queue
        self.queue = []
    
    #Pushes character onto stack
    def pushCharacter(self, ch):
        #Append() function to push element in the stack
        self.stack.append(ch)
    
    #Enqueue character in queue
    def enqueueCharacter(self, ch):
        #Append() function to queue element in queue
        self.queue.append(ch)
    
    #Pop character from stack
    def popCharacter(self):
        #Return character at the top of the stack (LIFO)
        return self.stack.pop()
        
    #Dequeue character from queue
    def dequeueCharacter(self):
        #Return first character in the queue (FIFO)
        return self.queue.pop(0)
    
#Main
def main():
    #User input for palindrome
    s = input()
    
    #Create the Solution class object
    obj = Solution()   
    
    #Get size of input
    l = len(s)
    
    #Push/enqueue all the characters of string s to stack
    for i in range(l):
        obj.pushCharacter(s[i])
        obj.enqueueCharacter(s[i])

    isPalindrome = True
    '''
    pop the top character from stack
    dequeue the first character from queue
    compare both the characters
    ''' 
    #Compare both characters from stack & queue
    for i in range(l // 2):
        if obj.popCharacter() != obj.dequeueCharacter():
            isPalindrome = False
            break
    
    #Print whether string is a palindrome or not
    if isPalindrome:
        print("The word, " + s + ", is a palindrome.")
    else:
        print("The word, " + s +", is not a palindrome.")    
        
#To run main() function
if __name__ == "__main__":
    main()