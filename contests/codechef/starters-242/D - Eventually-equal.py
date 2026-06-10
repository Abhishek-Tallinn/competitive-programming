# Problem: Starters 242 - Eventually equal
# Problem Link: https://www.codechef.com/START242D/problems/EQMNG


# cook your dish here
def solve():
    def gcd(a,b):
        if b == 0:
            return a
        return gcd(b,a%b)
    a,b,c = map(int,input().split())
    
    if a==b:
        print(0)
    elif gcd(a,c) == gcd(b,c):
        print(1)
    elif gcd(a,c+1) == gcd(b,c+1):
        print(2)
    else:
        print(3)




t = int(input())
for _ in range(t):
    solve()   

