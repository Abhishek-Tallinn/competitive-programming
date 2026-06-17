# Problem: Starters 243 - OR operations
# Problem Link: https://www.codechef.com/START243D/problems/OROPS

# cook your dish here
def solve():
    n = int(input())
    arr = [int(d) for d in input().split()]
    total = 0
    for num in arr:
        total|=num
    curr= 0
    groups = 0
    for num in arr:
        curr|=num
        if curr == total:
            groups+=1
            curr = 0
    print(len(arr) - groups)
