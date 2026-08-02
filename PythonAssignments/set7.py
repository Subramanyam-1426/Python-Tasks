# SET 7 — Higher Order Functions
#-------------------------------#
'''7.1 Apply Twice ⭐
apply_twice(lambda x: x + 3, 10)   ->  16
apply_twice(lambda x: x * 2, 5)    ->  20
apply_twice(str.upper, "hi")       ->  "HI" '''

# def apply_twice(fun,n):
#     n=fun(n)
#     return fun(n)

# print(apply_twice(lambda x: x + 3, 10))
# print(apply_twice(lambda x: x * 2, 5))
# print(apply_twice(str.upper, "hi") )

# -----------------------------------------------------------------------------------------------//

'''7.2 Function Composer ⭐⭐ 🔥
compose(f, g) returns a new function that computes f(g(x)).

add_one    = lambda x: x + 1
double     = lambda x: x * 2

f = compose(add_one, double)    # add_one(double(x))
print(f(5))                     # 11

g = compose(double, add_one)    # double(add_one(x))
print(g(5))                     # 12  '''

# def compose(f,g):
#     def fun(x):
#         return f(g(x))
#     return fun
  

# add_one    = lambda x: x + 1
# double     = lambda x: x * 2

# f = compose(add_one, double)    # add_one(double(x))
# print(f(5))                     # 11

# g = compose(double, add_one)    # double(add_one(x))
# print(g(5))                     # 12  

# ---------------------------------------------------------------------------------------------//

'''7.3 Menu Dispatch Table ⭐⭐
Replace a long if/elif chain with a dictionary of functions.

Input: 10 + 3   ->  13
Input: 10 - 3   ->  7
Input: 10 * 3   ->  30
Input: 10 / 3   ->  3.3333333333333335
Input: 10 % 3   ->  Unknown operator: %'''

# import operator

# operations = {"+" : operator.add, "-" : operator.sub, "*" : operator.mul, "/" : operator.truediv}

# def compute(s):
#     try:
#       s=s.split()
#       if s[1] in operations:
#          return operations[s[1]](int(s[0]),int(s[-1]))
#       else:
#          return f"Unknown operator : {s[1]}"
#     except (ValueError , IndexError) as error:
#        return "invalid input format , format should be - num1 operation num2"

# print(compute("10 + 3"))
# print(compute("10 - 3"))
# print(compute("10 * 3"))
# print(compute("10 / 3"))
# print(compute("10 % 3"))
# print(compute("10+3"))

# --------------------------------------------------------------------------------------------------//

'''7.4 IPL Player Sorter ⭐⭐⭐ 🔥
players = [
    {"name": "Kohli",   "runs": 741, "team": "RCB"},
    {"name": "Gill",    "runs": 890, "team": "GT"},
    {"name": "Rahul",   "runs": 616, "team": "LSG"},
    {"name": "Jaiswal", "runs": 625, "team": "RR"},
    {"name": "Samson",  "runs": 616, "team": "RR"},
]
Print three different sorted lists:

By runs (high to low):
  Gill      890
  Kohli     741
  Jaiswal   625
  Rahul     616
  Samson    616

By team, then runs (high to low):
  GT   Gill      890
  LSG  Rahul     616
  RCB  Kohli     741
  RR   Jaiswal   625
  RR   Samson    616

By name length:
  Gill, Kohli, Rahul, Samson, Jaiswal
For the two-key sort, use a tuple: key=lambda p: (p["team"], -p["runs"])'''


# players = [
#     {"name": "Kohli",   "runs": 741, "team": "RCB"},
#     {"name": "Gill",    "runs": 890, "team": "GT"},
#     {"name": "Rahul",   "runs": 616, "team": "LSG"},
#     {"name": "Jaiswal", "runs": 625, "team": "RR"},
#     {"name": "Samson",  "runs": 616, "team": "RR"},
# ]

# players.sort(key = lambda x : -x["runs"])
# print("Team   Name    Runs")
# for player in players:
#     print(f"{player["team"]}  {player["name"]}   {player["runs"]}" )

# print("---------------------")
# print("Team   Name    Runs")
# players.sort(key=lambda p : (p["team"], -p["runs"]))
# for player in players:
#     print(f"{player["team"]}  {player["name"]}   {player["runs"]}" )

# print("---------------------")
# players.sort(key=lambda p : len(p["name"]))
# for player in players:
#     print(f"{player["name"]}",end=" " )

# --------------------------------------------------------------------------------------------//

'''7.5 Text Cleaning Pipeline ⭐⭐⭐
Write pipeline(text, *operations) that applies each function in order and shows every step.

Input: "   Ravi Kumar Sharma   "
Operations: strip -> lowercase -> replace spaces with _ -> add "user_" prefix

Output:
Starting with: '   Ravi Kumar Sharma   '
  after clean          : 'Ravi Kumar Sharma'
  after to_lower       : 'ravi kumar sharma'
  after remove_spaces  : 'ravi_kumar_sharma'
  after add_prefix     : 'user_ravi_kumar_sharma'
Final: user_ravi_kumar_sharma'''

# def clean(t): return t.strip()
# def to_lower(t): return t.lower()
# def remove_spaces(t): return t.replace(" ", "_")
# def add_prefix(t): return f"user_{t}"

# def pipeline(text, *operations):
#     print(f"Starting with: {text}")
#     current = text
#     for op in operations:
#         current = op(current)
#         print(f"after {op.__name__} : {current}")
#     print(f"Final: {current}")
#     return current

# pipeline("   Ravi Kumar Sharma  ", clean, to_lower, remove_spaces, add_prefix)

# -------------------------------------------------------------------------------------------//

