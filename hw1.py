def hw1(n):
    if n <= 1:
        return n
    return hw1(n - 1) + hw1(n - 2)


def hw2(n):
    fib = [0, 1] + [0] * (n - 1)
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

print(hw1(38))