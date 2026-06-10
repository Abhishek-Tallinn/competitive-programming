# Problem: Starters 242 - Early certificates
# Problem Link: https://www.codechef.com/START242D/problems/EARLYWIN

# cook your dish here
def solve():
    n,m = map(int,input().split())
    a = input()
    b = input()
    i,j = 0,0
    ans = ""
    for i in range(len(min(a,b))):
        if a[i]==b[i]:
            ans+=a[i]
        else:
            break
    print(ans)
