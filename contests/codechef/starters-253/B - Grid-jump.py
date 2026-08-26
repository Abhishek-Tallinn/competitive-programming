# Problem: Starters 253- Grid jump
# Problem Link: https://www.codechef.com/START253C/problems/GRDJUMP
# cook your dish here
def solve():
    a,b,p,q,r = map(int,input().split())
    cost1 = cost2 = 0
    up_moves = (b+1)//2
    right_moves = (a+1)//2
    cost1 = up_moves*q + right_moves*p
    mn_cost = float('inf')
    x = y = 0
    for _ in range(min(a,b)):
        x+=1
        y+=1
        cost2+=r
        #cost2+= (r + ((a-x+1)//2)*p + ((b-y+1)//2)*q)
        mn_cost = min(mn_cost, cost2 + ((a-x+1)//2)*p + ((b-y+1)//2)*q)

    print(min(cost1,mn_cost))