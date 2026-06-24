# Problem: Starters 244- Carrot Collection
# Problem Link: https://www.codechef.com/problems/CARRCOL

# cook your dish here
def solve():
    n,l,r = map(int,input().split())
    arr = [int(d) for d in input().split()]
    patrol = set(range(l,r+1))
    #print(patrol)
    #available = []
    #for i in range(1,n+1):
    #    if i not in patrol:
    #        available.append(i)
    #print(arr)
    max_before = max_after = 0
    for i in range(0,l-1):
        max_before += arr[i]
    for j in range(r,n):
        max_after += arr[j]
    print(max(max_before,max_after))



t = int(input())
for _ in range(t):
    solve()