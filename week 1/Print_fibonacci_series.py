def fibonacci_series(n):
    #Print Fibonacci series values up to n
    a = 0
    b = 1

    while a <= n:
        print(a)
        a, b = b, a+b

#Calculate and return the factorial of n
def factorial(n):
    result = 1

    for i in range(1, n+1):
        result *= i

    return result

def main():
    num = int(input("Enter a number: "))

    print("Fibonacci series up to", num, ":")
    fibonacci_series(num)

    factorial_val = factorial(num)
    print("Factorial of", num, "is:", factorial_val)

if __name__ == "__main__":
    main()

