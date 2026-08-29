# Problem: Q2- Maximum valid split positions I
# Problem Link: https://leetcode.com/problems/maximum-valid-split-positions-i/

from math import gcd
class Solution:
    def maxValidSplits(self, nums: list[int]) -> int:
        def gcd(a,b):
            if b==0:
                return a
            return gcd(b,a%b)
        def score(b):
            m = len(b)
            if m<2:
                return 0
            pre = [0] * m
            suf = [0]*m
            pre[0] = b[0]
            for i in range(1,m):
                pre[i] = gcd(pre[i-1],b[i])
            suf[m-1] = b[m-1]
            for i in range(m-2,-1,-1):
                suf[i] = gcd(suf[i+1],b[i])
            return sum(1 for i in range(m-1) if pre[i]==suf[i+1])
        n = len(nums)
        best = score(nums)
        for r in range(n):
            best = max(best,score(nums[:r]+nums[r+1:]))
        return best