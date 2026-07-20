# Problem: DSA Monday 012 -  Candy distribution
# Problem Link: https://www.codechef.com/DSAMONDAY012/problems/CANDY01

n,c = map(int,input().split())
arr = [int(d) for d in input().split()]

if c >= sum(arr):
    print("Yes")
else:
    print("No")