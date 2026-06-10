# Problem: Starters 242 - Draft picks
# Problem Link: https://www.codechef.com/START242D/problems/DRAFTPICK


# cook your dish here
def solve():
    n,k = map(int,input().split())
    if k<=n:
        print(k)
        return
    gap = 0
    total = k
    i = k-1
    while i>0:
        if gap==2*(n-1):
            total+=i
            if i > 1:
                total+=i-1
            gap=0
            i-=2
        
        gap+=1
        i-=1
    print(total)