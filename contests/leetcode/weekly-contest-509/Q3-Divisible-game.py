# Problem: Q3 - Divisible Game
# Problem Link: https://leetcode.com/contest/weekly-contest-505/problems/divisible-game/


class Solution:
    def divisibleGame(self, nums: list[int]) -> int:
        MODULO = 10**9+7
        n = len(nums)
        divisors = set()
        for num in nums:
            i = 1
            while i*i<=num:
                if num%i==0:
                    a,b = i,num//i;
                    if a > 1:
                        divisors.add(a)
                    if b > 1:
                        divisors.add(b)
                i+=1
        k0 = 2
        while k0 in divisors:
            k0+=1
        candidates = divisors | {k0}
        best_diff = None
        best_k = None
        for k in candidates:
            cur = float('-inf')
            best_here = float('-inf')
            for num in nums:
                w = num if num%k==0 else -num
                cur = w if cur<0 else cur+w
                if cur > best_here:
                    best_here = cur
            if (best_diff is None or best_here > best_diff or
            (best_here == best_diff and k < best_k)):
                best_diff = best_here
                best_k = k
        return (best_diff * best_k)%MODULO