def function(x):
    ans = x**3 - 5*x + 1
    return ans

def dif_function(x):
    ans1 = 3*x**2 - 5
    return ans1

def newtonRaphson(x0, iter):
    for i in range(iter):
        fx = function(x0)
        fx_ = dif_function(x0)
        if fx_ == 0:
            print("Derivative is zero, Cannot continue")
            break
        else:
            x1 = x0 - fx / fx_
            x0 = x1
    print("Maximum no of iterations reached",x1)

def user_input():
    x = float(input("Enter the value of x: "))
    n = int(input("Enter the no of iterations: "))
    newtonRaphson(x, n)

def main():
    user_input()

if __name__ == "__main__":
    main()

