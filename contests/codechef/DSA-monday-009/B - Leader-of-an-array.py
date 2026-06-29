# Problem: DSA Monday 009 - Leader of an array
# Problem Link: https://www.codechef.com/DSAMONDAY009/problems/DSACPR49


# cook your dish here

n = int(input())
arr = [int(d) for d in input().split()]

ans = [arr[-1]]
mx = arr[-1]
for i in range(len(arr)-2,-1,-1):
    if arr[i]>mx:
        mx = arr[i]
        ans.append(arr[i])
        
print(*ans[::-1])