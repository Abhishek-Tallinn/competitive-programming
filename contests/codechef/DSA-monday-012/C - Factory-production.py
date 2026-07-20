# Problem: DSA Monday 012 -  Factory Production
# Problem Link: https://www.codechef.com/DSAMONDAY012/problems/FCTPR

# cook your dish here
n,x = map(int,input().split())
arr = [int(d) for d in input().split()]

def is_feasible(time:int,arr:list)->bool:
    total_items = 0
    for a in arr:
        total_items+=time//a
        if total_items>=x:
            return True
    return total_items>=x
        
arr.sort()
mn_time = 1
mx_time = arr[-1] * x
while mn_time < mx_time:
    mid = (mn_time+mx_time)//2
    if is_feasible(mid,arr):
        mx_time = mid
    else:
        mn_time = mid+1
print(mn_time)