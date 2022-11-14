n = 100

def fibonacci_iterative():
    n1 = 0
    n2 = 1
    nth = n1 + n2

    for i in range(n):
        n1 = n2
        n2 = nth
        nth = n1 + n2
    return nth

def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

c= {}
def fibonacci_mas_optimo (n):
    if n < 2:
        return n
    if n in c:
        return c[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    c[n] = res
    return res
