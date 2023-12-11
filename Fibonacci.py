def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n+1):
        # print(i)
        value=fib[i-1]+fib[i-2]
        fib.append(value)
        # fib.append(fib[i-1]+fib[i-2])
    return fib

input=10
fibo=fibonacci(input)
print(fibo)