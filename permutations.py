def factorial(n):
    r = 1
    for i in range (1, n + 1):
        r *= i
    return r

def main():
    sz = int(input("Enter the size of the list: "))
    perm = int(input("Enter the permutation number: "))
    maxperm = factorial(sz)
    if perm > maxperm:
        print("The maximum permutation for a list of size", sz, "is", maxperm)

    numlist = list(range(1,sz+1))

if __name__ == "__main__":
    main()
