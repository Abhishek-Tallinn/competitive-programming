# Problem: Starters 252- Mex and Max
# Problem Link: https://www.codechef.com/START252C/problems/MEXMAX7
# cook your dish here
from collections import Counter
def solve():
    n = int(input())
    arr = [int(d) for d in input().split()]
    MOD = 998244353
    cnt = Counter(arr)
    max_val = max(arr)
    ans = 0
    prefix_prod = [0]*(max_val+2)
    if cnt[0]>0:
        prefix_prod[0] = pow(2,cnt[0],MOD)-1
    for k in range(1,max_val+1):
        if cnt[k]==0 or prefix_prod[k-1] == 0:
            prefix_prod[k]=0
        else:
            prefix_prod[k] = prefix_prod[k-1] * (pow(2,cnt[k],MOD)-1)%MOD
    for k in range(max_val+1):
        ans = (ans+prefix_prod[k])%MOD
    for k in range(1,max_val+1):
        if cnt[k]==0:
            continue
        ways_k = pow(2,cnt[k],MOD)-1
        if k == 1:
            contrib = ways_k
        else:
            if prefix_prod[k-2]==0:
                continue
            contrib = prefix_prod[k-2]* ways_k % MOD
        ans = (ans+contrib)%MOD
    print(ans)





t = int(input())
for _ in range(t):
    solve()