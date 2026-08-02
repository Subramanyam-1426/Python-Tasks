'''SET 8 — Lambda / Anonymous Functions
8.1 One-Liner Pack ⭐
Write each as a single lambda:

is_even(10)        ->  True
is_leap(2024)      ->  True
is_leap(1900)      ->  False
reverse("python")  ->  "nohtyp"
bigger(10, 20)     ->  20
area_circle(7)     ->  153.93804002589985'''

# is_even=lambda n : n%2==0
# is_leap=lambda n: n%4==0 and (n%100!=0 or n%400==0)
# reverse = lambda s: s[::-1]
# bigger = lambda a, b: max(a, b)
# area_circle = lambda r: __import__('math').pi * r**2

# print(is_even(10))        
# print(is_leap(2024))      
# print(is_leap(1900))      
# print(reverse("python"))  
# print(bigger(10, 20))     
# print(area_circle(7))     

# ----------------------------------------------------------------------------------------------------//

'''8.2 Grade Machine ⭐⭐
One lambda using chained ternaries.

grade(95) ->  A
grade(82) ->  B
grade(65) ->  C
grade(45) ->  D
grade(20) ->  F
Cutoffs: 90+ A, 75+ B, 60+ C, 40+ D, else F.'''

# grade = lambda s: 'A' if s >= 90 else 'B' if s >= 75 else 'C' if s >= 60 else 'D' if s >= 40 else 'F'

# print(grade(95))
# print(grade(82))
# print(grade(65))
# print(grade(45))
# print(grade(20))

# -----------------------------------------------------------------------------------------------------//

'''8.3 Case-Insensitive Sort ⭐⭐
Input:  ["banana", "Apple", "cherry", "Date"]
Output: ['Apple', 'banana', 'cherry', 'Date']'''

# fruits = ["banana", "Apple", "cherry", "Date"]
# sorted_fruits = sorted(fruits, key=lambda s: s.lower())

# print(sorted_fruits)

# ----------------------------------------------------------------------------------------------------//

'''8.4 The Lambda Loop Trap 🔥 ⭐⭐⭐
Run this. Explain the output in a comment. Then fix it.

funcs = []
for i in range(3):
    funcs.append(lambda: i * 10)

print([f() for f in funcs])
Buggy output   : [20, 20, 20]
Expected output: [0, 10, 20]'''

# funcs = []
# for i in range(3):
#     # FIX: Bind the current value of i to a default argument x
#     funcs.append(lambda x=i: x * 10)

# print([f() for f in funcs])

# Explanation:
# The original code prints [20, 20, 20] due to Python's "late binding" behavior.
# The lambdas look up the variable 'i' in the outer scope only when they are called,
# not when they are created. By the time the list comprehension runs, the loop
# has finished, and 'i' remains stuck at its final value of 2.
# 
# The fix binds 'i' as a default argument (x=i) at creation time, freezing its 
# value for each unique lambda function instance.

# -------------------------------------------------------------------------------------------------//

'''8.5 When NOT to Use Lambda ⭐⭐
Take this unreadable lambda and rewrite it as a proper def with a docstring. Both must give the same output.

process = lambda d: {k: (v * 2 if isinstance(v, int) else v.upper() if isinstance(v, str) else v) for k, v in d.items()}

print(process({"a": 5, "b": "hi", "c": 3.5}))
Output: {'a': 10, 'b': 'HI', 'c': 3.5}'''

# def process(data_dict):
#     result = {}
#     for key, value in data_dict.items():
#         if isinstance(value, int):
#             result[key] = value * 2
#         elif isinstance(value, str):
#             result[key] = value.upper()
#         else:
#             result[key] = value
#     return result

# print(process({"a": 5, "b": "hi", "c": 3.5}))

# ---------------------------------------------------------------------------------------------------------//


