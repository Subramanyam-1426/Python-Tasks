# SET 6 — Factorial using Recursion
# ----------------------------------#

'''6.1 The Classic ⭐
factorial(5)  ->  120
factorial(0)  ->  1
factorial(10) ->  3628800'''

def fact(n):
    if n<2:
        return 1
    return n*fact(n-1)

n=int(input())
print(fact(n))

# --------------------------------------------------------------------------------------------//

'''6.2 Visual Trace Printer ⭐⭐ 🔥
Print what happens at every level. This one problem will teach you recursion permanently.

Input: 4

Output:
factorial(4) called
needs 4 * factorial(3) ... waiting
|  factorial(3) called
|  needs 3 * factorial(2) ... waiting
|  |  factorial(2) called
|  |  needs 2 * factorial(1) ... waiting
|  |  |  factorial(1) called
|  |  |  BASE CASE -> returning 1
|  |  got 1, so 2 * 1 = 2
|  got 2, so 3 * 2 = 6
got 6, so 4 * 6 = 24

Final answer: 24
Pass a depth parameter and use "|  " * depth as padding.'''

def factorial(n, depth=0):
    pad = "|  " * depth
    print(f"{pad}factorial({n}) called")

    if n == 0 or n == 1:
        print(f"{pad}BASE CASE -> returning 1")
        return 1

    print(f"{pad}needs {n} * factorial({n-1}) ... waiting")
    sub = factorial(n - 1, depth + 1)
    result = n * sub
    print(f"{pad}got {sub}, so {n} * {sub} = {result}")
    return result

print("\nFinal answer:", factorial(4))

# --------------------------------------------------------------------------------------------//
'''6.3 The Negative Trap ⭐⭐
Run factorial(-5) on the naive version (no validation). Note down the exact error. Then explain in a comment: why doesn't it stop?

Then fix it.

Before fix: RecursionError: maximum recursion depth exceeded
After fix : ValueError: Factorial is not defined for negative numbers'''

def fact(n):
    if n<0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n*fact(n-1)
try:
  n=int(input())
  print(fact(n))
except ValueError as error:
    print(error)

# -----------------------------------------------------------------------------------------------//

'''6.4 Recursive Power ⭐⭐
power(2, 10)  ->  1024
power(5, 0)   ->  1
power(3, 4)   ->  81
Then write fast_power(x, n) using divide-and-conquer and compare the number of calls.

fast_power(2, 30)  ->  1073741824'''

def power(a,b):
    if b==0:
        return 1
    half=power(a,b//2)
    if b%2==0:
        print(half*half)
        return half*half
    print(half*half*a)
    return half*half*a  

print(power(2,10))
print(power(2,0))
print(power(3,4))
print(power(2,30))

# ----------------------------------------------------------------------------------------------//

'''6.5 Double Factorial ⭐⭐⭐
n!! = n x (n-2) x (n-4) x ... down to 1 or 2.

Input: 8   ->  384      (8 x 6 x 4 x 2)
Input: 7   ->  105      (7 x 5 x 3 x 1)
Input: 1   ->  1
Input: 0   ->  1'''

# def df(n):
#     if n==0 or n==1:
#         return 1
#     return n*df(n-2)

# print(df(8))
# print(df(7))
# print(df(1))
# print(df(0))

# ------------------------------------------------------------------------------------------------//
