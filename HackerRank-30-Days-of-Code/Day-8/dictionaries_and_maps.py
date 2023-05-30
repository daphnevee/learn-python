"""
Python 3 program to utilize Key-Value pair mappings using a Map or Dictionary data structure

Task: Given n names and phone numbers, assemble a phone book that maps friends' names
to their respective phone numbers. You will then be given an unknown number of names
to query your phone book for. For each name queried, print the associated entry
from your phone book on a new line in the form name=phoneNumber; if an entry for name
is not found, print Not found instead.

Note: Your phone book should be a Dictionary/Map/HashMap data structure.

Input:
n = 3
entry 1 = sam 99912222
entry 2 = tom 11122222
entry 3 = harry 12299933
query 1 = sam
query 2 = edward
query 3 = harry

Output:
query 1 = sam -> sam=99912222
query 2 = edward -> Not found
query 3 = harry -> harry=12299933

"""
#Main
def main():
    #User input for no. of entries in phone book
    n = int(input())
    #Constraint: 1 <= n <= 10^5
    if (n >= 1 and n <= 100001):
        #Create dictionary
        phonebook = {}
        for i in range(n):
            #User input for phonebook entries
            first_name, phone_number = str(input()).split()
            phonebook[first_name] = phone_number
        #Constraint: 1 <= queries <= 10^5
        query = 0
        for query in range(1, 100001):
            #Try-except block to handle EOF Error
            try:
                #User input for phonebook name query
                name = str(input())
            except EOFError as e:
                break
            #Check if name is in phonebook
            if name in phonebook.keys():
                print("{}={}".format(name, phonebook.get(name)))
            else:
                print("Not found")
    else: 
        print("No. of entries should be between 1 to 10^5")
        
#To run main() function
if __name__ == "__main__":
    main()
