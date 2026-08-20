# Problem: DSA Monday 016 -  Server queue
# Problem Link: https://www.codechef.com/DSAMONDAY016/problems/SQUEU

# cook your dish here
from bisect import bisect_left

# cook your dish here
def solve():
    n,m,c = map(int,input().split())
    capacities = [c]*m
    requests = [int(d) for d in input().split()]
    def can_serve(start_idx):
        server_count = 1
        current_cap = c
        for i in range(start_idx,len(requests)):
            req = requests[i]
            if req>c:
                return False
            if current_cap>=req:
                current_cap-=req
            else:
                server_count+=1
                current_cap = c-req
            if server_count > m:
                return False
        return server_count<=m
                          

    lo,hi = 0 , len(requests)
    ans = len(requests)
    while lo< hi:
        mid = (lo+hi)//2
        if can_serve(mid):
            #ans = mid
            hi = mid
        else:
            lo = mid+1
    print(lo)
        



solve()