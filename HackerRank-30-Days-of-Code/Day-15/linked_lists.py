"""
Python 3 program to utilize Linked Lists

Task: Complete the insert function in your editor so that it creates
a new Node (pass data as the Node constructor argument) and inserts it
at the tail of the linked list referenced by the head parameter. Once
the new node is added, return the reference to the head node.

Note: The head argument is null for an empty list.

Input:
STDIN  Function 
-----  --------
4      T = 4
2      first data = 2
3
4
1      fourth data = 1

Output:
2 3 4 1

"""
#Node class
class Node:
    #Constructor
    def __init__(self, data):
        self.data = data
        self.next = None
        
#Solution class
class Solution:
    #Display node
    def display(self, head):
        current = head
        #Start from head of list
        while current:
            #Print linked list
            print(current.data, end = ' ')
            current = current.next
            
    #Insert node at tail of linked list
    def insert(self, head, data):
        #Instantiate new node
        new_node = Node(data) 
        #Base Case: If linked list is empty, set node as head
        if head == None:
            head = new_node
        else:
            #Set pointer to head
            current = head
            #Traverse list until tail is reached
            while current.next:
                current = current.next
            #Insert new node after tail is reached (no next node)
            current.next = new_node
        return head
    
#Main
def main():
    #Instance variable of Solution class
    mylist = Solution()
    #User input for no. of nodes
    T = int(input())
    #Initialize head of empty linked list
    head = None
    #User input for data of linked list
    for i in range(T):
        data = int(input())
        #Insert data at tail of linked list (referenced by head)
        head = mylist.insert(head, data)
    #Return reference to head node once new node is added
    mylist.display(head)
    
#To run main() function
if __name__ == "__main__":
    main()