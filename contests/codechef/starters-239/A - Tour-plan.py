# Problem: Starters 239  - Tour plan
# Problem Link: https://www.codechef.com/problems/TOURPLAN?tab=statement

x,y,z = map(int,input().split())

print(x+max(z-50,0)*y)
