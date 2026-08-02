import random
print(random.randint(1, 10))

# **Why it happened:**
# > Python searches for modules in the current folder before checking its built-in libraries.
#  Since I created a file named `random.py`, Python imported my file instead of the built-in `random` module.
#  My file didn't have the `randint()` function, so it raised an `AttributeError`.

# **How to fix it:**
# > Rename the file to something other than `random.py` (for example, `myrandom.py`) and delete the `__pycache__` folder. 
# Then run the program again so Python imports the actual built-in `random` module.
