# Problem: Q2 - Maximum valid pair sum
# Problem Link: https://leetcode.com/contest/biweekly-contest-186/problems/maximum-valid-pair-sum


class Solution:
    def maxValidPairSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        best = 0
        mx = 0 
        for j in range(k,n):
            best = max(best,nums[j-k])
            mx = max(mx,best+ nums[j])

        return mx