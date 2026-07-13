# Problem: DSA Monday 011 -  Chocolate squares
# Problem Link: https://www.codechef.com/DSAMONDAY011/problems/CHOCO1


# cook your dish her
import math
def solve():
    l,b = map(int,input().split())
    area = l*b
    mx = 0
    
    #for i in range(1,min(l,b)):
    #    if l%i == 0 and b%i==0:
    #        mx = i
    print(math.gcd(l,b))
        



t = int(input())
for _ in range(t):
    solve()