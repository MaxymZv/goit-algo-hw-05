def fibonacci_cashing():             #Creating function to cash fibonacci 
    cash = {}                        #Creating empty dictionary
    def fibonacci(n: int):           #Creating function to calculate fibonacci
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n in cash:
            return cash[n]
        cash[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cash[n]               #Returning cashed fibonacci 
    return fibonacci                 #returning inner function

fib = fibonacci_cashing()

print(fib(10))
print(fib(15))
