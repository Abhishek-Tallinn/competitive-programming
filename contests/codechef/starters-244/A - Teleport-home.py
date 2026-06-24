# Problem: Starters 244- Teleport home
# Problem Link: https://www.codechef.com/problems/TELHOME

# cook your dish here
d,t = map(int,input().split())
if t>=d:
    print(0)
else:
    print(d-t)