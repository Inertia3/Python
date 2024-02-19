import numpy as np

def function(x):
    ans = x*3 - x*2 - 1
    return ans

def bisectionMethod(a, b, n):
    for i in range(n):
        x = (a + b) / 2
        if function(x) > 0:
            b = x
        else:
            a = x
    print("The root is:", x)


def main():
    a = float(input("First Approximation root: "))
    b = float(input("Second Approximation root: "))
    if function(a) * function(b) > 0:
        print("Given approximate roots do not bracket the root.")
        print("Try again with different approximate values.")
    else:
        n = int(input("Number of iterations: "))
        bisectionMethod(a, b, n)

if __name__ == "_main_":
    main()

    #Switching up to feature3 to check the git rebase 
    #Making changes here and merging it to the main branch