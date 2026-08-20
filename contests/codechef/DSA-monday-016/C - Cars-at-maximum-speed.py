# Problem: DSA Monday 016 -  Cars at maximum speed
# Problem Link: https://www.codechef.com/DSAMONDAY016/problems/CATMS
# cook your dish here
def solve():
    n = int(input())
    speeds = [int(d) for d in input().split()]
    cnt = 0
    mn = float('inf')
    for i in range(len(speeds)):
        if speeds[i] < mn:
            mn = min(mn,speeds[i])
            cnt+=1
    print(cnt)
        