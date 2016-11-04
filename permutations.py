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
    
    #If the permutation we're looking for is greater than the possible number of permutations
    #then subtract the length of the list from the permutation number
    if (perm >= fact*sz):
        perm -= sz
        
    #To determine the value to use, we take the floor of the permutation divided by the number
    #of permutations that begin with the same value. This gives us the index of the value to place.
    #For example, if we're looking for the 6th permutation of a list of length 4, then the first 
    #6 elements begin with 1, the next 6 begin with 2, etc... So this code takes the floor of 6/6, 
    #which is 1, so we look at index 1 for the value, which is 2.
    first = math.floor(perm/fact)
    lstnew = lst[:]
    
    #Here we remove the element we just used
    lstnew.remove(lstnew[first])
    
    
    if perm >= fact:
        perm -= fact
    return str(lst[first]) + str(get_perm(lstnew, perm))

def main():
    sz = int(input("Enter the size of the list: "))
    perm = int(input("Enter the permutation number: "))
    maxperm = factorial(sz)
    if perm > maxperm:
        print("The maximum permutation for a list of size", sz, "is", maxperm)

    numlist = list(range(1,sz+1))
    permstr = get_perm(numlist, perm)
    print("Permutation number", perm, "is", permstr)

if __name__ == "__main__":
    main()
