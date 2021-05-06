def fib(number):
    if number > 0:
        return fib(number - 1) + fib(number - 2)

print(fib(6))