# Problem: Q3 - Count valid sequences
# Problem Link: https://leetcode.com/problems/count-valid-sequences/

class Solution:
    def countValidSequences(self, n: int, k: int) -> int:
        modulo = 10**9+7
        mx = n + 1
        factorial = [1] * mx
        for i in range(1,mx):
            factorial[i] = factorial[i-1]* i % modulo
        inverse_fact = [1] * mx
        inverse_fact[mx-1] = pow(factorial[mx-1],modulo-2,modulo)
        for i in range(mx-2,-1,-1):
            inverse_fact[i] = inverse_fact[i+1] * (i+1)%modulo
        def comb(n,r):
            if r<0 or r>n:
                return 0
            return factorial[n] * inverse_fact[r] % modulo * inverse_fact[n-r] % modulo
        total = comb(n-1,k-1)
        odds = 0
        if (n+k)%2 == 0:
            odds = comb((n+k)//2-1,k-1)
        res = (total - odds + modulo) % modulo
        return res