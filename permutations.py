#Zachary Collins and Laura Tebben

#TO RUN:
#run $python permutations.py
#Enter the size of the list to be permuted (e.g. {1, 2, 3, 4} has size 4)
#Enter the permutation you wish to find, keeping in mind numbering starts at 0

import math

#Function to find the factorial of any given number. 
#Used to determine the number of permutations that start with the same value
def factorial(n):
    r = 1
    for i in range (1, n + 1):
        r *= i
    return r

#Gets the kth permutation
def get_perm(lst, perm):
    #Get the length of the list that is being permuted
    sz = len(lst)

    #If it only contains 1 element, return that element
    if sz == 1:
        return lst[0]
    
    #Calculate the factorial of the size of the list minus 1 to determine the number 
    #of permutations that start with the same value
    fact = factorial(sz-1)
    
    #To determine the value to use, we take the floor of the permutation divided by the number
    #of permutations that begin with the same value. This gives us the index of the value to place.
    #For example, if we're looking for the 6th permutation of a list of length 4, then the first 
    #6 elements begin with 1, the next 6 begin with 2, etc... So this code takes the floor of 6/6, 
    #which is 1, so we look at index 1 for the value, which is 2.
    first = math.floor(perm/fact)
    lstnew = lst[:]
    
    #Here we remove the element we just used
    lstnew.remove(lstnew[first])
    
    #Here we subtract the number of permutations that start with same value from the permutation
    #we're looking for, until perm falls within the first (n-1)! items. Since we are calling this function
    #recursively, this scales the permutation to the smaller list.
    while (perm >= fact):
        perm -= fact
    return str(lst[first]) + " " + str(get_perm(lstnew, perm))

def main():
    #Get user inputs
    sz = int(input("Enter the size of the list: "))
    perm = int(input("Enter the permutation number: "))
    
    #Calculate the maximum number of permutations and display an error message if the requested permutation
    #is greater than the max
    maxperm = factorial(sz) - 1
    if perm > maxperm:
        print("The range of permutations for a list of size", sz, "is 0 to", maxperm)
        exit()
    
    #Build the list of 1 to n elements
    numlist = list(range(1,sz+1))
    
    #Call get_perm to get the requested permutation, and print the result
    permstr = get_perm(numlist, perm)
    print("Permutation number", perm, "is [", permstr,"]")

if __name__ == "__main__":
    main()

    
    #Example runs:
    #Enter the size of the list: 4
    #Enter the permutation number: 6
    #Permutation number 6 is [ 2 1 3 4 ]
    
    #Enter the size of the list: 4
    #Enter the permutation number: 19
    #Permutation number 19 is [ 4 1 3 2 ]
    
    #Enter the size of the list: 3
    #Enter the permutation number: 4
    #Permutation number 4 is [ 2 3 1 ]

    #Bonus question 2
    #This program can handle lists of large sizes:
    #Enter the size of the list: 20
    #Enter the permutation number: 153
    #Permutation number 153 is [ 1 2 3 4 5 6 7 8 9 10 11 12 13 14 16 17 18 19 20 15 ]
    
    #Discussion:
    #The factorial function is the biggest contributor to the performance of this program.
    #Because factorial(n) only goes through the for loop one time, this is complexity O(n). 
    #This means that n is the quantity that the performance relies most on. Inside the get_perm() 
    #function, we call factorial(n) n times. So program complexity is O(n^2).
