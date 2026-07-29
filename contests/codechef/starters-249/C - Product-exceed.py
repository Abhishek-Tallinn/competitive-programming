# Problem: Starters 249- Product exceed
# Problem Link: https://www.codechef.com/START249D/problems/PRDEXC

# cook your dish here
import math
def solve():
    x,y,p = map(int,input().split())
    ops = 0
    if x*y>=p:
        print(0)
        return
    mx= max(x,y)
    mn = min(x,y)

    target = (p+(mx-1))//mx
    ops1 = target - mn
    
    
    t = math.isqrt(p)
    if t<=mx:
        print(ops1)
        return
    if t*t<p:
        t+=1
    if t * (t-1) >=p:
        ops2= (t-1-mn) + t-mx
    else:
        ops2 = t-mn + t-mx
    print(min(ops1,ops2))