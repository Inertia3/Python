def function(x):
    ans = x**3 - 5*x + 1
    return ans

def secantMethod(x0, x1, iterations):
    for i in range(iterations):
        fx0 = function(x0)
        fx1 = function(x1)
        x2 = x1 - ((x1 - x0) / (fx1 - fx0)) * fx0
            
        x0 = x1
        x1 = x2
    print(x2)


def main():
    x0 = float(input("Enter First Guess: "))
    x1 = float(input("Enter Second Guess: "))
    iterations = int(input("Enter Number of Iterations: "))
    secantMethod(x0, x1, iterations)

if __name__ == "__main__":
    main()


