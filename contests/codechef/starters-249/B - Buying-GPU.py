# Problem: Starters 249- Buying GPU
# Problem Link: https://www.codechef.com/START249D/problems/GPUBUY

# cook your dish here
import math
def solve():
    x,y,z = map(int,input().split())
    if y>=z:
        print(-1)
        return
    rate = z-y
    print((x+rate-1)//rate)
    return
