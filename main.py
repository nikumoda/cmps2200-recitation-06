def fib_recursive(n, counts):
    """
    Return the nth Fibonacci number. 
    counts is a list of n+1 elements, where counts[i] is incremented
    each time fib_recursive(i, counts) is called.
    """    
    counts[n] += 1
    # base cases
    if n <= 1:
        return n
    # recursive case
    return fib_recursive(n-1, counts) + fib_recursive(n-2, counts)

    
    
def fib_top_down(n, fibs):
    # return memoized value if present
    if fibs[n] != -1:
        return fibs[n]
    # base cases
    if n <= 1:
        fibs[n] = n
        return fibs[n]
    # compute, memoize, and return
    fibs[n] = fib_top_down(n-1, fibs) + fib_top_down(n-2, fibs)
    return fibs[n]


def fib_bottom_up(n):
    # handle small n
    if n <= 1:
        return n
    # build table bottom-up
    fibs = [0] * (n + 1)
    fibs[1] = 1
    for i in range(2, n + 1):
        fibs[i] = fibs[i - 1] + fibs[i - 2]
    return fibs[n]




