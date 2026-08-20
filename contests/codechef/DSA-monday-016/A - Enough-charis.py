# Problem: DSA Monday 016 -  Enough chairs
# Problem Link: https://www.codechef.com/DSAMONDAY016/problems/PWTHC

# cook your dish here
n,k,p = map(int,input().split())

if n*k >= p:
    print("Yes")
else:
    print("No")