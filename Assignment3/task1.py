def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

n = input('Enter a number: ')
print(f'Factorial of {n} is: ', factorial(int(n)))
