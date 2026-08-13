# Problem: Starters 251- Make multiple
# Problem Link: https://www.codechef.com/problems/MUL123
# cook your dish here
def solve():
    n = int(input())
    ops = 0
    if n%3==0:
        print(0)
        return
    next_higher = n+1
    while next_higher%5!=0:
        next_higher+=1
    if (n+1)%3==0 or next_higher%3==0:
        print(1)
        return
    print(2)




t = int(input())
for _ in range(t):
    solve()