# ===== 10.1.py =====
# 10.1 Map Warm-Ups ⭐

numbers = [1, 2, 3, 4, 5]
print(f"Squares of [1,2,3,4,5]                  ->  {list(map(lambda x: x**2, numbers))}")

values = ["1", "2", "3", "42"]
print(f'["1","2","3","42"] to integers          ->  {list(map(int, values))}')

names = ["ravi", "priya"]
print(f'["ravi","priya"] to uppercase           ->  {list(map(str.upper, names))}')

words = ["hi", "python", "is"]
print(f'Lengths of ["hi","python","is"]         ->  {list(map(len, words))}')

# ===== 10.2.py =====
# 10.2 Temperature Converter ⭐ 

celsius = [0, 25, 37, 100, -40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))

print("Input: ", celsius, " (Celsius)")
print("Output:", fahrenheit, " (Fahrenheit)")

# ===== 10.3.py =====
# 10.3 Two Lists at Once ⭐⭐

names = ["Ravi", "Priya", "Kiran"]
marks = [78, 92, 45]

result = list(map(lambda name, mark: f"{name}: {mark}", names, marks))
print("Output:", result)

names2 = ["Ravi", "Priya", "Kiran", "Anu"]
marks2 = [78, 92]

result2 = list(map(lambda name, mark: f"{name}: {mark}", names2, marks2))
print("Different lengths:", result2)

# ===== 10.4.py =====
# 10.4 Reduce Warm-Ups ⭐⭐

from functools import reduce

nums = [1, 2, 3, 4, 5]
total = reduce(lambda x, y: x + y, nums)
print("Sum of [1,2,3,4,5]                 ->", total)

product = reduce(lambda x, y: x * y, nums)
print("Product of [1,2,3,4,5]             ->", product)

nums2 = [3, 7, 2, 9, 4]
maximum = reduce(lambda x, y: x if x > y else y, nums2)
print("Maximum of [3,7,2,9,4]             ->", maximum)

words = ["Python", "is", "powerful"]
sentence = reduce(lambda x, y: x + " " + y, words)
print('Join ["Python","is","powerful"]     ->', f'"{sentence}"')

words2 = ["hi", "python", "is"]
longest = reduce(lambda x, y: x if len(x) > len(y) else y, words2)
print('Longest word in ["hi","python","is"] ->', f'"{longest}"')

# ===== 10.5.py =====
# 10.5 Word Frequency Counter ⭐⭐⭐ 🔥

from functools import reduce

words = ["apple", "banana", "apple", "cherry", "banana", "apple"]

def count_word(acc, word):
    acc[word] = acc.get(word, 0) + 1
    return acc

result = reduce(count_word, words, {})

print('Input: ', words)
print('Output:', result)

# ===== 10.6.py =====
from functools import reduce

sales = [
    {"product": "Laptop", "price": 55000, "qty": 3, "region": "South"},
    {"product": "Mouse", "price": 500, "qty": 20, "region": "North"},
    {"product": "Monitor", "price": 12000, "qty": 5, "region": "South"},
    {"product": "Keyboard", "price": 1500, "qty": 12, "region": "South"},
    {"product": "Printer", "price": 8000, "qty": 2, "region": "North"},
]

south_sales = filter(lambda x: x["region"] == "South", sales)
south_revenue = map(lambda x: x["price"] * x["qty"], south_sales)
south_total = reduce(lambda x, y: x + y, south_revenue)

north_sales = filter(lambda x: x["region"] == "North", sales)
north_revenue = map(lambda x: x["price"] * x["qty"], north_sales)
north_total = reduce(lambda x, y: x + y, north_revenue)

print(f"Total South revenue: Rs {south_total:,}")
print(f"Total North revenue: Rs {north_total:,}")

south_one_line = sum(x["price"] * x["qty"] for x in sales if x["region"] == "South")
north_one_line = sum(x["price"] * x["qty"] for x in sales if x["region"] == "North")

print(f"Total South revenue: Rs {south_one_line:,}")
print(f"Total North revenue: Rs {north_one_line:,}")

# The generator expression with sum() is more readable because it performs filtering, revenue calculation, and summation compactly in one expression.

# ===== 10.7.py =====
# 10.7 Sum of Squares of Evens ⭐⭐⭐

from functools import reduce

def sum_of_squares(start, end):
    evens = filter(lambda x: x % 2 == 0, range(start, end + 1))
    squares = map(lambda x: x ** 2, evens)
    return reduce(lambda x, y: x + y, squares)

print("Input:  1 to 10")
print("Output:", sum_of_squares(1, 10))

print("\nInput:  1 to 100")
print("Output:", sum_of_squares(1, 100))

