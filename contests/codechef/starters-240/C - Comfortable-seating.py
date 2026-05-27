# Problem: Starters 240  - Comfortable seating
# Problem Link: https://www.codechef.com/problems/CYCYC


# cook your dish here
def solve():
    n = int(input())
    fr = [int(d) for d in input().split()]
    n = len(fr)
    min_value = min(fr)
    if fr.count(min_value) == 1:
        print("No")
        return
    print("Yes")