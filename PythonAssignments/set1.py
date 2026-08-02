# Input:  [6, 12, 4, 0, 15, 8, 3, 20]

# Output:
# Total runs      : 68
# Highest over    : 20
# Lowest over     : 0
# Average per over: 8.5
# Maiden overs    : 1
# Bytes used      : 32


def stats(cricket):
    sums,high,maiden,avg=0,0,0,0
    maxi=max(cricket)
    mini=min(cricket)
    for i in range (len(cricket)):
        sums+=cricket[i]
        if cricket[i]==0:
            maiden+=1
    avg=sums/len(cricket)
    print("Total runs : ",sums)
    print("Highest : ",maxi)
    print("Lowest over : ",mini)
    print("Average per score : ",avg)
    print("Maiden overs : ",maiden)
    print("Bytes Used : ",len(cricket)*4)

cricket=list(map(int,input().split()))
stats(cricket)

# Start with array('i', [10, 20, 30, 40, 50]) and apply these operations in order. Print the array after each step.

# Operations:
#   1. append 60
#   2. insert 15 at index 1
#   3. remove the value 30
#   4. pop the element at index 0
#   5. reverse

# Output:
# After append  : array('i', [10, 20, 30, 40, 50, 60])
# After insert  : array('i', [10, 15, 20, 30, 40, 50, 60])
# After remove  : array('i', [10, 15, 20, 40, 50, 60])
# After pop     : array('i', [15, 20, 40, 50, 60])  (popped 10)
# After reverse : array('i', [60, 50, 40, 20, 15])

from array import array
def arraysurgery(a):
    a=array('i',a)
    a.append(60)
    print(a)
    a.insert(1,15)
    print(a)
    a.remove(30)
    print(a)
    a.pop(0)
    print(a)
    a.reverse()
    print(a)

a=list(map(int,input().split()))
arraysurgery(a)

# 1.3 Second Highest Scorer ⭐⭐ 🔥
# Find the second largest element without using sort() or sorted().

# Input:  [45, 88, 12, 88, 67, 90]
# Output: Second largest = 88

# Input:  [5, 5, 5]
# Output: No second largest

from ast import Call
import sys
def secondlargest(a):
    sl=0

    maxi=max(a)
    for i in range(len(a)):
        if a[i]<maxi:
            sl=max(sl,a[i])
    if sl!=0:
        print(sl)
    else:
        print("No second largest")
        
a=list(map(int,input().split()))
secondlargest(a)

# 1.4 Left Rotate by K ⭐⭐
# Rotate an array to the left by k positions.

# Input:  arr = [1, 2, 3, 4, 5, 6, 7],  k = 3
# Output: [4, 5, 6, 7, 1, 2, 3]

# Input:  arr = [1, 2, 3],  k = 5
# Output: [3, 1, 2]

def leftrotate(a,k):
    while(k>0):
        l=a[0]
        for i in range(0,len(a)):
            if i==len(a)-1:
                a[i]=l
            else:
                a[i]=a[i+1]
        k-=1
    return a


a=list(map(int,input().split()))
k=int(input())
print(leftrotate(a,k))

# 1.5 Merge Two Sorted Arrays ⭐⭐⭐
# Merge two already-sorted arrays into one sorted array — without using sorted().

# Input:  a = [1, 4, 7, 9],  b = [2, 3, 8, 10, 15]
# Output: [1, 2, 3, 4, 7, 8, 9, 10, 15]

def sorting(a,b):
    p1,p2,k=0,0,0
    ans=[0]*((len(a))+(len(b)))
    while(p1<len(a) and p2<len(b)):
        if a[p1]<b[p2]:
            ans[k]=a[p1]
            p1+=1
        else:
            ans[k]=b[p2]
            p2+=1
        k+=1
    while(p1<len(a)):
        ans[k]=a[p1]
        p1+=1
        k+=1
    while(p2<len(b)):
            ans[k]=b[p2]
            p2+=1
            k+=1
    return ans

a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(sorting(a,b))
