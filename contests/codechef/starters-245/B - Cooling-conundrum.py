# Problem: Starters 245 - Cooling Conundrum
# Problem Link: https://www.codechef.com/problems/COOLCON


# cook your dish here

def solve():
    x,y = map(int,input().split())
 
    time = 0
    while x>y:
        time+=(x+9)//10
        x-=1

    print(time)




t = int(input())
for _ in range(t):
    solve()