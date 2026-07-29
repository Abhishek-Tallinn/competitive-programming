# Problem: Starters 249- Up Down palindrome
# Problem Link: https://www.codechef.com/START249D/problems/UPDWPAL

from collections import Counter
def solve():
    n = int(input())
    arr = [int(d) for d in input().split()]
    def is_palindrome(arr):
        if arr==arr[::-1]:
            return True
        return False
    if is_palindrome(arr):
        print("Yes")
        return
    valid_vs = None
    for i in range(n//2):
        a,b = arr[i],arr[n-1-i]
        if a==b:
            continue
        if (abs(a-b))!=2:
            print("No")
            return
        mn = min(a,b)
        pair_vs = {mn,mn+1}
        if valid_vs is None:
            valid_vs = pair_vs
        else:
            valid_vs&=pair_vs
        if not valid_vs:
            print("no")
            return
    
        
    for v in valid_vs:
        if v in arr:
            print("Yes")
            return
    print("No")
    