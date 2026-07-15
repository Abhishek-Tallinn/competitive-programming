# Problem: Starters 246- Fair flipping
# Problem Link: https://www.codechef.com/START247D/problems/FLIP2K

def solve():
    n,k = map(int,input().split())
    s = input()
    c0 = s.count('0')
    c1 = n-c0
    if c0<k or c1<k:
        print(s)
        return 
    if n>2*k:
        print('0'*c0 + '1'*c1)
        return
    complement = ''.join('1' if ch=='0' else'0' for ch in s)
    print(min(s,complement))
        



t = int(input())
for _ in range(t):
    solve()