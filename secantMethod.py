def function(x):
    ans = x*3 - x*2 - 1
    return ans

def dif_function(x):
    ans1 = 3*x**2 - 2*x
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

if __name__ == "_main_":
    main()



# def function(x):
#     return x*3 - x*2 - 2

# def secant_method(x0, x1, max_iter=100):
#     for i in range(max_iter):
#         f_x0 = function(x0)
#         f_x1 = function(x1)
#         if f_x1 == 0:
#             print("Root found:", x1)
#             return x1
#         if f_x0 == f_x1:
#             print("Secant method fails.")
#             return None
#         x_next = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
#         x0, x1 = x1, x_next
#     print("Maximum iterations reached. No root found.")
#     return None

# def user_input():
#     x0 = float(input("Enter the first initial guess: "))
#     x1 = float(input("Enter the second initial guess: "))
#     secant_method(x0, x1)

# def main():
#     user_input()

# if _name_ == "_main_":
#     main()