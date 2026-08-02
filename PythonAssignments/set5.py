
# SET 5 — Recursion
# 5.1 Digit Sum ⭐
# Input: 12345   ->  Output: 15
# Input: 9       ->  Output: 9
# Input: 100     ->  Output: 1

def digit_sum(n,s):
    if n==0:
        return s
    else:
        r=n%10
        s+=r
        return digit_sum(n//10,s)
print(digit_sum(12345,0))
print(digit_sum(100,0))

# 5.2 Reverse a String ⭐
# Input: "DriveReady"  ->  Output: "ydaeRevirD"
# Input: "a"           ->  Output: "a"
# No slicing shortcut s[::-1]. Use recursion.

def reverse(s,n):
    if n>=len(s)//2:
        return s
    else:
        s[n],s[len(s)-n-1]=s[len(s)-n-1],s[n]
    return reverse(s,n+1)
s="goodmorning"
s1=list(s)
s2=reverse(s1,0)
s1="".join(s2)
print(s1)

# 5.3 Palindrome Checker ⭐⭐
# Ignore spaces and case.

# Input: "madam"              ->  True
# Input: "Never odd or even"  ->  True
# Input: "python"             ->  False
# Input: "Was it a car or a cat I saw"  ->  True
def palind(s,n):
    if n>=len(s)//2:
        return s
    else:
        s[n],s[len(s)-n-1]=s[len(s)-n-1],s[n]
    return palind(s,n+1)
s="goodmorning"
s1=list(s)
s2=palind(s1,0)
s1="".join(s2)
if s1==s1:
    print("The string is palindrome")
else:
    print("The string is not palindrome")


# 5.4 Tower of Hanoi ⭐⭐⭐ 🔥
# Print every move and the total count.

# Input: 3 disks (A -> C using B)

# Output:
# Move disk 1: A -> C
# Move disk 2: A -> B
# Move disk 1: C -> B
# Move disk 3: A -> C
# Move disk 1: B -> A
# Move disk 2: B -> C
# Move disk 1: A -> C
# Total moves: 7
# For n disks the count should be 2^n - 1. Verify with n = 4 (should be 15)

def hanoi(n, src, des, temp):
    if (n == 0):
        return
    hanoi(n-1, src, temp, des)
    print(f"Move disk {n}: {src} -> {des}")
    hanoi(n-1, temp, des, src)


src = 'A'
des = 'C'
temp = 'B'
n = 3
hanoi(n, src, des, temp)
print(f"Total moves: {2**n-1}")
n = 4
hanoi(n, src, des, temp)
print(f"Total moves: {2**n-1}")
