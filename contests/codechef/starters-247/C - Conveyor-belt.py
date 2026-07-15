# Problem: Starters 246- Conveyor belt
# Problem Link: https://www.codechef.com/START247D/problems/CONVEYOR

def solve():
    n,p = map(int,input().split())
    s = input()
    mn_moves = float('inf')
    if s[p-1] == 'R':
        mn_moves = min(s[:(p-1)].count('R')+1,s[p:].count('L'))
    elif s[p-1]=='L':
        mn_moves = min(s[:(p-1)].count('R'), s[p:].count('L')+1)
    print(mn_moves)



t = int(input())
for _ in range(t):
    solve()