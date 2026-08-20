# Problem: DSA Monday 016 -  Maximum divisor score
# Problem Link: https://www.codechef.com/DSAMONDAY016/problems/MADIS

# cook your dish here
from collections import defaultdict
def solve():
    n = int(input())
    nums = [int(d) for d in input().split()]
    
    MAX = max(nums)+1
    d = [0] * MAX
    for div in range(1,MAX):
        for multiple in range(div,MAX,div):
            d[multiple] += 1
    
    best = defaultdict(int)
    ans = 0
    for x in nums:
        score = d[x]
        candidates = [x-1,x+1,2*x,3*x]
        if x%2==0: candidates.append(x//2)
        if x%3==0: candidates.append(x//3)
        
        prev_best = 0
        for c in candidates:
            if c in best:
                prev_best = max(prev_best,best[c])
        dp_i = score + prev_best
        best[x] = max(best[x],dp_i)
        ans = max(ans,dp_i)
    print(ans)
    