# Problem: Starters 246- Alternating arrays
# Problem Link: https://www.codechef.com/START247D/problems/ALTARR

def solve():
    n = int(input())
    arr = [int(d) for d in input().split()]
    start_odd = start_even = 0
    for i in range(len(arr)):
        if i%2==0:
            if arr[i]%2 == 1:
                start_even+=1
            elif arr[i]%2==0:
                start_odd+=1
        elif i%2==1:
            if arr[i]%2==1:
                start_odd+=1
            elif arr[i]%2==0:
                start_even+=1
    print(min(start_even,start_odd))



t = int(input())
for _ in range(t):
    solve()