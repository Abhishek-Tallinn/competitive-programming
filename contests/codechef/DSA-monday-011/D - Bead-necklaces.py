# Problem: DSA Monday 011 -  Bead necklaces
# Problem Link: https://www.codechef.com/DSAMONDAY011/problems/NECK

n = int(input())
arr = [int(d) for d in input().split()]

n = len(arr)

is_pal = [[False]*n for _ in range(n)]
for i in range(n):
    is_pal[i][i] = True #base case as single character is palindrome
for i in range(n-1):
    is_pal[i][i+1] = (arr[i] ==arr[i+1])

for length in range(3,n+1):
    for i in range(n-length+1):
        j = i+length-1
        is_pal[i][j] = (arr[i] == arr[j]) and is_pal[i+1][j-1]
        
inf = float('inf')
dp = [inf] * n
for i in range(n):
    if is_pal[0][i]:
        dp[i] = 1
    else:
        for j in range(1,i+1):
            if is_pal[j][i] and dp[j-1]!=inf:
                dp[i] = min(dp[i],dp[j-1]+1)
print(dp[n-1])