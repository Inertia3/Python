import numpy as np

def f(x):
    ans = x**2-2*x+3
    return ans

def bisectionMethod(a,b,n):
    for i in range (n):
        x1 = (a+b)/2
        if(f(x1)>0):
            b = x1
        else:
            a = x1
    print("The root is: "+x1)

def main():
    a = int(input("Enter the first guess: "))
    b = int(input("enter the second guess: "))

    if(f(a) * f(b) > 0):
        print("The given approximation do not bracket the roots:")
        print("Try again with different roots")
    else:
        n = int(input("Enter the no of iterations to be performed"))
        bisectionMethod(a,b,n)

if __name__ == "__main__":
    main()