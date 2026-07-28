# Problem: DSA Monday 013 -  Maximize wood value
# Problem Link: https://www.codechef.com/DSAMONDAY013/problems/ROCU

# cook your dish here
def solve():
    n = int(input())
    prices = [int(d) for d in input().split()]
    
    dp = [0] * (n+1) #base
    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i] = max(dp[i],prices[j-1] + dp[i-j])
    print(dp[n])
    