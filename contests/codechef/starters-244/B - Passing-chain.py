# Problem: Starters 244- Passing Chain
# Problem Link: https://www.codechef.com/problems/PASSCHAIN


# cook your dish here
def solve():
    n,k = map(int,input().split())
    ball_pos = 1
    for i in range(1,n+1,k):
        if i+k > n:
            break
        ball_pos = i + k
    print(ball_pos)








t = int(input())
for _ in range(t):
    solve()