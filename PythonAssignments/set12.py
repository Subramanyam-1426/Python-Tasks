# SET 12 — Decorators
# 12.1 Shout Decorator ⭐
# @uppercase converts the returned string to uppercase.

# @uppercase
# def greet(name):
#     return f"hello, {name}"

# print(greet("ravi"))   # HELLO, RAVI
def uppercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase
def greet(name):
    return f"hello, {name}"

print(greet("Hasini"))  

# 12.2 Call Counter ⭐⭐
# @count_calls
# def say_hi():
#     print("Hi!")

# say_hi()
# say_hi()
# say_hi()
# print(say_hi.count)
# Output:
# Call #1
# Hi!
# Call #2
# Hi!
# Call #3
# Hi!
# 3
def count_calls(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        print(f"Call #{wrapper.count}")
        return func(*args, **kwargs)
    wrapper.count = 0
    return wrapper

@count_calls
def say_hi():
    print("Hi!")

say_hi()
say_hi()
say_hi()
print(say_hi.count)

# 12.3 The Timer ⭐⭐ 🔥
# @timer
# def slow_sum(n):
#     return sum(range(n))

# print(slow_sum(1_000_000))
# Output:
# [TIMER] slow_sum took 0.0201s
# 499999500000

def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[TIMER] slow_sum took {end_time - start_time:.4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))

print(slow_sum(1_000_000))

# 12.4 The Three Rules 🔥 ⭐⭐⭐
# Write a decorator that deliberately breaks all three rules, then fix them one at a time and record what changed:

# Rule broken	What goes wrong
# No *args, **kwargs	?
# No return result	?
# No @wraps(func)	?

from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Expected after all fixes:")
        result = func(*args, **kwargs)
        return result
    return wrapper

@my_decorator
def add(a, b):
    """Adds two numbers."""
    return a + b

print(add(3, 5))
print(add.__name__)
print(add.__doc__)

# 12.5 Login Required ⭐⭐⭐
# admin = {"name": "Ravi", "logged_in": True}
# guest = {"name": "Anon", "logged_in": False}

# @require_login
# def view_dashboard(user):
#     return f"Welcome {user['name']}!"

# print(view_dashboard(admin))   # Welcome Ravi!
# print(view_dashboard(guest))   # Access denied. Please log in.

admin = {"name": "Ravi", "logged_in": True}
guest = {"name": "Anon", "logged_in": False}

def require_login(func):
    def wrapper(user, *args, **kwargs):
        if user.get("logged_in"):
            return func(user, *args, **kwargs)
        else:
            return "Access denied. Please log in."
    return wrapper

@require_login
def view_dashboard(user):
    return f"Welcome {user['name']}!"

print(view_dashboard(admin))
print(view_dashboard(guest))

# 12.6 Repeat N Times ⭐⭐⭐ 🔥
# A decorator that takes an argument — three layers.

# @repeat(3)
# def greet(name):
#     print(f"Hello, {name}!")

# greet("Priya")
# Output:
# Hello, Priya!
# Hello, Priya!
# Hello, Priya!
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

greet("Priya")


# 12.7 Stacking Order 🔥 ⭐⭐⭐
# @bold
# @italic
# def text():
#     return "Hello"
# print(text())        # ?

# @italic
# @bold
# def text2():
#     return "Hello"
# print(text2())       # ?
# Output:
# <b><i>Hello</i></b>
# <i><b>Hello</b></i>
# Write one line explaining why the order flips.


def bold(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<b>{result}</b>"
    return wrapper

def italic(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return f"<i>{result}</i>"
    return wrapper

@bold
@italic
def text():
    return "Hello"
print(text())        

@italic
@bold
def text2():
    return "Hello"
print(text2())       

# 12.8 Cache the Fibonacci ⭐⭐⭐
# Write your own @cache decorator. Then compare:

# Without cache: fib(35) took about 3 seconds
# With cache   : fib(35) took about 0.0000 seconds
# With cache   : fib(100) = 354224848179261915075
# Then replace yours with @functools.lru_cache and confirm the same result.

import time
from functools import wraps, lru_cache

# 1. WITHOUT CACHE

def fib_without_cache(n):
    if n <= 1:
        return n
    return fib_without_cache(n - 1) + fib_without_cache(n - 2)


start = time.perf_counter()
result = fib_without_cache(35)
end = time.perf_counter()

print("Without cache:")
print("fib(35) =", result)
print(f"Time = {end - start:.4f} seconds")

# 2. OUR OWN @cache DECORATOR

def cache(func):
    memory = {}

    @wraps(func)
    def wrapper(*args):
        if args in memory:
            return memory[args]
        result = func(*args)
        memory[args] = result
        return result
    return wrapper

@cache
def fib_with_cache(n):
    if n <= 1:
        return n
    return fib_with_cache(n - 1) + fib_with_cache(n - 2)

start = time.perf_counter()
result = fib_with_cache(35)
end = time.perf_counter()

print("\nWith our @cache:")
print("fib(35) =", result)
print(f"Time = {end - start:.4f} seconds")

print("fib(100) =", fib_with_cache(100))

# 3. USING functools.lru_cache

@lru_cache(maxsize=None)
def fib_lru(n):
    if n <= 1:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)

start = time.perf_counter()
result = fib_lru(35)
end = time.perf_counter()

print("\nWith @lru_cache:")
print("fib(35) =", result)
print(f"Time = {end - start:.4f} seconds")

print("fib(100) =", fib_lru(100))

