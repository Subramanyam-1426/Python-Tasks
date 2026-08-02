
# Write place_order(customer, *items, **charges).

# place_order("Ravi", "Biryani", "Coke", "Gulab Jamun",
#             delivery=40, gst=25, discount=50)
# Output:
# Customer : Ravi
# Items ordered (3):
#   1. Biryani
#   2. Coke
#   3. Gulab Jamun
# Charges:
#   delivery : 40
#   gst      : 25
#   discount : 50

def place_order(customer,*items,**charges):
    print("customer : ",customer)
    print(f"Items ordered ({len(items)}):")
    for i in range(len(items)):
        print(f"{i+1}.{items[i]}")
    print("Charges: ")
    for k,v in charges.items():
        print(f"{k} : {v}")
    

customer=input()
place_order(customer,"biryani","coke","gulab jamun",delivery=40,gst=25,discount=50)

# 2.2 Flexible Calculator ⭐
# calculator(a, b, op="+") supporting + - * /.

# calculator(10, 5)         ->  15
# calculator(10, 5, "-")    ->  5
# calculator(10, 5, "*")    ->  50
# calculator(10, 0, "/")    ->  Error: cannot divide by zero
# calculator(10, 5, "%")    ->  Error: unknown operator '%'

def caluculator(a,b,op):
    match op:
        case '+': print(a+b) 
        case '-':print(a-b)
        case '*':print(a*b)
        case '/':print(a/b)
a,b=map(int,input().split())
op=input()
caluculator(a,b,op)

# build_query(**filters) turns keyword arguments into a URL query string.

# build_query(city="hyderabad", rating=4, veg=True)
# ->  city=hyderabad&rating=4&veg=True

# build_query()
# ->  (empty string)

def build(**filters):
    if( not len(filters)):
        print("empty string")
    else:
        arr=[]
        for a,b in filters.items():
            arr.append(f"{a}={b}")
        print("&".join(arr))
build(city="hyderabad",rating=4,veg=True)

# This code is broken. Run it, observe the bug, explain why in a comment, then fix it.

def add_to_cart(item, cart=[]):
    if(len(cart)):
        cart.pop()
    cart.append(item)
    return cart

print(add_to_cart("pen"))
print(add_to_cart("book"))
print(add_to_cart("bag"))

# ccept a name, any number of marks, and optional details.

# report("Priya", 85, 92, 78, 90, section="A", year=2)
# Output:
# Student : Priya
# Section : A
# Year    : 2
# Marks   : 85, 92, 78, 90
# Total   : 345
# Average : 86.25
# Result  : PASS
# Pass mark = average >= 40.
def report(name,*marks,**details):
    print("Student : ",name)
    for k,v in details.items():
        print(k," : ",v)
    for i in marks:
        print(i,end=" ")
    print()
    print(f"Total : {sum(marks)}")
    print(f"Average : {sum(marks)/len(marks)}")
    if sum(marks)/len(marks)>=40:
        print(f"Result : PASS")
    else:
        print(f"Result : FAIL")
s=input()
report(s,89,87,76,74,section="A",year=2)

# 2.6 Predict, Then Run 🔥 ⭐⭐⭐
# Write your prediction as a comment before running.

def mystery(a, b=[], *c, **d):
    b.append(a)
    return a, b, c, d

print(mystery(1))
print(mystery(2, [9]))
print(mystery(3))
print(mystery(4, [7], 8, 9, x=10))
#output
# (1, [1], (), {})
# (2, [9, 2], (), {})
# (3, [1, 3], (), {})
# (4, [7, 4], (8, 9), {'x': 10})
