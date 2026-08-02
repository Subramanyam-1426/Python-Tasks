
# 3.1 Scope Puzzle Pack ⭐⭐ 🔥
# For each snippet: write your predicted output as a comment, run it, then write one line explaining what happened.

# Puzzle A

x = 10
def f():
    print(x)
    x = 20
f()
#10
# Puzzle B

x = 5
def f(x):
    x = 10
f(x)
print(x)
#5
# Puzzle C

x = "global"
def outer():
    x = "enclosing"
    def inner():
        print(x)
    inner()
outer()

#enclosing
# Puzzle D

if True:
    z = 99
print(z)
#99


# 3.2 Movie Ticket Counter ⭐⭐
# Use a global variable to track seats.

# Total seats: 100

# book(3)   ->  Booked 3 seats. Remaining: 97
# book(10)  ->  Booked 10 seats. Remaining: 87
# book(200) ->  Only 87 seats left. Booking failed.
# cancel(5) ->  Cancelled 5 seats. Remaining: 92
# status()  ->  92 seats available out of 100

ts = 100
total = 100

def book(n):
    global ts
    if n <= ts:
        ts -= n
        print(f"Booked {n} seats. Remaining: {ts}")
    else:
        print(f"Only {ts} seats left. Booking failed.")

def cancel(n):
    global ts
    if ts + n <= total:
        ts += n
    else:
        ts = total
    print(f"Cancelled {n} seats. Remaining: {ts}")

def status():
    print(f"{ts} seats available out of {total}")

# Example
book(3)
book(10)
book(200)
cancel(5)
status()
