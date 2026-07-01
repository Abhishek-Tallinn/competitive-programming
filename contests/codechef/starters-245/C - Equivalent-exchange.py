# Problem: Starters 245- Equivalent exchange
# Problem Link: https://www.codechef.com/problems/EQEXCH


# cook your dish here
def solve():
    n,k = map(int,input().split())
    stones = [int(d) for d in input().split()]
    total = 0
    mn = mx = 0
    for stone in stones:
        total+=stone
        mn = min(mn,total)
        mx = max(mx,total)
    if -mn <= k-mx:
        print("yes")
    else:
        print("No")



t = int(input())
for _ in range(t):
    solve()