# Problem: DSA Monday 011 -  Shopping and coins
# Problem Link: https://www.codechef.com/DSAMONDAY011/problems/GTRAIN

# cook your dish here
def solve():
    n = int(input())
    costs = [2*int(d) for d in input().split()]
    coins = [int(x) for x in input().split()]
    total_coins = 0
   
    inf = float('inf')
    dp = [inf]*(max(costs) +1 )
    dp[0] = 0
    for coin in coins:
        for amount in range(coin,max(costs)+1):
            if dp[amount-coin] + 1 < dp[amount]:
                dp[amount] = dp[amount-coin]+1
    total_coins = sum(dp[c] for c in costs)
    print(total_coins)
    
t = int(input())
for _ in range(t):
    solve()