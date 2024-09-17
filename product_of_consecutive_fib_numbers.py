def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a


def product_fib(_prod):
    n = 0
    while True:
        fibn = fib(n)
        fibn1 = fib(n + 1)
        if fibn * fibn1 == _prod:
            return [fibn, fibn1, True]
        if fibn * fibn1 > _prod:
            return [fibn, fibn1, False]

        n += 1

