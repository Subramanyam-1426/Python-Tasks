# 11.1 Power Factory ⭐⭐
def make_power(n):
    def power(x):
        return x ** n
    return power


square = make_power(2)
cube = make_power(3)

print(square(5))         # 25
print(cube(3))           # 27
print(make_power(4)(2))  # 16


# 11.2 Independent Counters ⭐⭐🔥
def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


c1 = make_counter()
c2 = make_counter()

print(c1(), c1(), c1())   
print(c2(), c2())         
print(c1())               


# 11.3 Running Average ⭐⭐⭐
def make_averager():
    total = 0
    count = 0

    def average(n):
        nonlocal total, count
        total += n
        count += 1
        return total / count

    return average

avg = make_averager()
print(avg(10))
print(avg(20))
print(avg(30))
print(avg(40))

# 11.4 Closure Stack ⭐⭐⭐
def make_stack():
    stack = []

    def push(x):
        stack.append(x)
        print(f"Pushed {x}. Size: {len(stack)}")

    def pop():
        if stack:
            x = stack.pop()
            print(f"Popped {x}. Size: {len(stack)}")
        else:
            print("Stack is empty")

    def size():
        print(len(stack))

    return push, pop, size


push, pop, size = make_stack()

push(10)
push(20)
push(30)
pop()
pop()
size()
pop()
pop()

# 11.5 Call Me Once ⭐⭐⭐🔥
def once(func):
    result = None
    called = False

    def wrapper():
        nonlocal result, called
        if not called:
            result = func()
            called = True
        return result

    return wrapper


def expensive_setup():
    print("Running setup...")
    return "DONE"


setup = once(expensive_setup)

print(setup())
print(setup())
print(setup())


# 11.6 UPI Wallet ⭐⭐⭐
def create_wallet(name, balance):

    def deposit(amount):
        nonlocal balance
        if amount > 0:
            balance += amount
            print(f"Deposited {amount}. Balance: {balance}")
        else:
            print("Deposit must be positive")

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            print(f"Insufficient funds. Balance: {balance}")
        else:
            balance -= amount
            print(f"Withdrew {amount}. Balance: {balance}")

    def statement():
        print(f"{name}'s balance: {balance}")

    return deposit, withdraw, statement


deposit, withdraw, statement = create_wallet("Ravi", 1000)

statement()
deposit(500)
withdraw(2000)
withdraw(300)
deposit(-100)
statement()