def recursion(n):
    if n==2: return 2
    return n + recursion(n-1)
print(recursion(5))
print(recursion(10))
print(recursion(20))