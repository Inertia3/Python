def f(x):
    return 3*x**3 - 2*x**2 +10

def secantMethod(x0, x1, n):
    for i in range(n):
        fx0 = f(x0)
        fx1 = f(x1)

        x2 = x1 - ((x1 -x0)/ (fx1 - fx0)) * fx0

        x0 = x1
        x1 = x2
    print("The root of the equation is:", x2)

def main():
    x0 = int(input("Enter the initail guess:"))
    x1 = int(input("Enter the second guess:"))
    n = int(input("Enter the no of iteration:"))

    secantMethod(x0, x1, n)

if __name__ == "__main__":
    main()

