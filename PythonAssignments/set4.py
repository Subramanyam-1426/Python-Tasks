
# 4.1 Factorial Table ⭐
# Output:
#   n |                        n! | digits
# ----+---------------------------+-------
#   0 |                         1 |      1
#   1 |                         1 |      1
#   2 |                         2 |      1
#   3 |                         6 |      1
#   4 |                        24 |      2
#   5 |                       120 |      3
#  ...
#  15 |         1,307,674,368,000 |     13
# Print 0 to 15. Use {:,} for comma formatting.

import math

for n in range(16):
    fact = math.factorial(n)
    digits = len(str(fact))
    print(n, fact, digits)

# 4.2 Trailing Zeros 🔥 ⭐⭐⭐
# Find the number of trailing zeros in n! without computing the factorial.

# Input: 10   ->  Output: 2      (10! = 3628800)
# Input: 25   ->  Output: 6
# Input: 100  ->  Output: 24
# Input: 1000 ->  Output: 249
# Hint: a trailing zero comes from a factor of 10 = 2 × 5. There are always more 2s than 5s, so just count the 5s: n//5 + n//25 + n//125 + ...

n = int(input())

count = 0

while n > 0:
    n = n // 5
    count += n

print(count)

# .3 Permutations and Combinations ⭐⭐
# Write nPr(n, r) and nCr(n, r).

# nPr(5, 2)   ->  20
# nCr(5, 2)   ->  10
# nCr(15, 11) ->  1365
# nCr(52, 5)  ->  2598960     (poker hands!)
# nCr(5, 7)   ->  Error: r cannot be greater than n
import math
def ncr(n,r):
    if r>n:
        print("Error: r cannot be greater than n")
        return
    nf=math.factorial(n)
    rf=math.factorial(r)
    lf=math.factorial(n-r)
    print(nf/(rf*lf))

def npr(n,r):
    nf=math.factorial(n)
    rf=math.factorial(r)
    print(nf/rf)
npr(5, 2)
ncr(5, 2)  
ncr(15, 11) 
ncr(52, 5)  
ncr(5, 7) 

# 4.4 Compute e ⭐⭐⭐
# Use the series e = 1/0! + 1/1! + 1/2! + 1/3! + ... for 20 terms.

# Output:
# Terms used : 20
# Computed e : 2.718281828459045
# math.e     : 2.718281828459045
# Difference : 0.00e+00
# Try it with only 5 terms and then 10 terms. Watch how fast it converges.


import math

terms = 20
e = 0

fact = 1
for i in range(terms):
    if i > 0:
        fact *= i
    e += 1 / fact

print("Terms used :", terms)
print("Computed e :", e)
print("math.e     :", math.e)
print("Difference :", "{:.2e}".format(abs(math.e - e)))


# 4.5 Input Validator ⭐⭐
# Write a factorial function that rejects bad input properly.

# factorial(5)      ->  120
# factorial(0)      ->  1
# factorial(-3)     ->  ValueError: Factorial is not defined for negative numbers
# factorial(2.5)    ->  TypeError: Expected an integer, got float
# factorial("five") ->  TypeError: Expected an integer, got str

def factorial(n):
    if not isinstance(n, int):
        raise TypeError(f"Expected an integer, got {type(n).__name__}")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")

    fact = 1
    for i in range(1, n + 1):
        fact *= i

    return fact


# Test cases
print(factorial(5))
print(factorial(0))

try:
    print(factorial(-3))
except Exception as e:
    print(type(e).__name__ + ":", e)

try:
    print(factorial(2.5))
except Exception as e:
    print(type(e).__name__ + ":", e)

try:
    print(factorial("five"))
except Exception as e:
    print(type(e).__name__ + ":", e)
