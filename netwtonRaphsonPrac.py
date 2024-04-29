def f(x):
    return x**2 + 4

def diff_f(x):
    return 2*x

def newtonRaphson(x, iter):
    for i in range(iter):
        fx = f(x)
        fx_ = diff_f(x)
        if fx_ == 0:
            print("Derivative is zero, Cannot continue")
            break
        else:
            x1 = x - fx / fx_
            if abs(x1 - x) < 0.0001:  # Checking convergence
                print("Convergence achieved:", x1)
                break
            x = x1
    else:
        print("Maximum number of iterations reached")

def main():
    n = int(input("Enter the number of iterations: "))
    x = float(input("Enter the initial guess: "))  # Convert input to float
    newtonRaphson(x, n)

if __name__ == "__main__":
    main()



    