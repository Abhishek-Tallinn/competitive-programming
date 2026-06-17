# Problem: Starters 243 - Interesting match
# Problem Link: https://www.codechef.com/START243D/problems/INTMTCH

# cook your dish here
x,y = map(int,input().split())
if abs(x-y)<=2:
    print("Interesting")
else:
    print("Boring")