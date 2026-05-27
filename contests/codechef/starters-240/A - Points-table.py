# Problem: Starters 240  - Points table
# Problem Link: https://www.codechef.com/problems/POINTT

# cook your dish here
x,y,a,b = map(int,input().split())
if x>a:
    print("Alice")
elif x<a:
    print("Bob")
else:
    if y>b:
        print("Alice")
    elif y<b:
        print("Bob")
    else:
        print("Alice")