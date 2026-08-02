# # SET 9 — filter()
# ------------------ #

'''9.1 Filter Warm-Ups ⭐
Numbers divisible by 7 from 1 to 50
->  [7, 14, 21, 28, 35, 42, 49]

Words longer than 4 letters from ["hi", "python", "is", "great", "ok"]
->  ['python', 'great']

Palindromes from ["madam", "python", "level", "code", "radar"]
->  ['madam', 'level', 'radar']'''

# # 1. Numbers divisible by 7 from 1 to 50
# nums = range(1, 51)
# div_by_7 = list(filter(lambda x: x % 7 == 0, nums))
# print(div_by_7)

# # 2. Words longer than 4 letters
# words = ["hi", "python", "is", "great", "ok"]
# long_words = list(filter(lambda s: len(s) > 4, words))
# print(long_words)

# # 3. Palindromes from a list
# strings = ["madam", "python", "level", "code", "radar"]
# palindromes = list(filter(lambda s: s == s[::-1], strings))
# print(palindromes)

# ----------------------------------------------------------------------------------------------------//

'''9.2 Clean the Junk ⭐⭐
Use filter(None, ...).

Input:  [0, 1, "", "hello", None, [], [1,2], False, True, 0.0, "0"]
Output: [1, 'hello', [1, 2], True, '0']
Explain in a comment: why did "0" survive but 0 did not?'''

# junk_list = [0, 1, "", "hello", None, [], [1,2], False, True, 0.0, "0"]
# clean_list = list(filter(None, junk_list))

# print(clean_list)

# Explanation:
# Passing 'None' as the function argument to filter() tells Python to drop all 
# elements that evaluate to False in a boolean context (falsy values).
# 
# The numeric value 0 evaluates to False, so it is filtered out. 
# The string "0" is a non-empty string, and all non-empty strings evaluate to 
# True in Python, so it survives the filter.

# ------------------------------------------------------------------------------------------------------//

'''9.3 Above Average Students ⭐⭐⭐ 🔥
Filter students who scored above the class average.

students = [
    {"name": "Ravi",   "marks": 78},
    {"name": "Priya",  "marks": 92},
    {"name": "Kiran",  "marks": 45},
    {"name": "Divya",  "marks": 88},
    {"name": "Suresh", "marks": 61},
]
Output:
Class average: 72.8
Above average:
  Priya  92
  Divya  88
  Ravi   78
You need two passes — compute the average first, then filter.'''

# students = [
#     {"name": "Ravi",   "marks": 78},
#     {"name": "Priya",  "marks": 92},
#     {"name": "Kiran",  "marks": 45},
#     {"name": "Divya",  "marks": 88},
#     {"name": "Suresh", "marks": 61},
# ]

# total_marks = sum(student["marks"] for student in students)
# average = total_marks / len(students)

# above_avg_students = list(filter(lambda s: s["marks"] > average, students))
# above_avg_students.sort(key=lambda s: s["marks"], reverse=True)

# print(f"Class average: {average:.1f}")
# print("Above average:")
# for student in above_avg_students:
#     print(f"  {student['name']:<7} {student['marks']}")

# --------------------------------------------------------------------------------------//

'''9.4 Prime Filter ⭐⭐
Input:  range(1, 51)
Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
Write is_prime as a proper def, not a lambda. Explain why in a comment.'''

# def is_prime(n: int) -> bool:
#     if n < 2:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# # Use filter with the prime checking function
# prime_numbers = list(filter(is_prime, range(1, 51)))
# print(prime_numbers)

''' Returns True if a number is prime, False otherwise.
    Explanation for using a proper def over a lambda:
    Lambdas are restricted to a single expression and cannot contain multi-line 
    logic, loops (like 'for' or 'while'), or early 'return' statements. Checking 
    for primality requires iterating through potential divisors and breaking out 
    early if a factor is found, which is unreadable or impossible in a lambda. '''

# ------------------------------------------------------------------------------------------------//

'''9.5 The Exhaustion Trap 🔥 ⭐⭐
Run this and explain the second output.

result = filter(lambda x : x > 3, [1, 2, 3, 4, 5])
print(list(result))
print(list(result))
Output:
[4, 5]
[]
Then fix it so both prints show [4, 5].'''

# result = list(filter(lambda x: x > 3, [1, 2, 3, 4, 5]))
# print(result)
# print(result)

'''Key point: filter(), map() all return iterators, which are consumed after one complete iteration. 
   Converting them to a list preserves the values for repeated use.'''

# ----------------------------------------------------------------------------------------------------//
