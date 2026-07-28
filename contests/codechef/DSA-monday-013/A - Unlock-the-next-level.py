# Problem: DSA Monday 013 -  Unlock the next level
# Problem Link: https://www.codechef.com/DSAMONDAY013/problems/UTNL


# cook your dish here
x,y = map(int,input().split())

if y>=x:
    print("UNLOCKED")
else:

    print(x-y)