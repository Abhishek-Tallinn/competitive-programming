# Problem: Q1 - Sum of Integers with Max Digit Range
# Problem Link: https://leetcode.com/contest/weekly-contest-505/problems/sum-of-integers-with-max-digit-range/


class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        mx_range = 0
        range = []
        for num in nums:
            mx = 0
            mn = float('inf')
            for d in str(num):
                mx = max(mx,int(d))
                mn = min(mn,int(d))
            mx_range = max(mx_range,mx-mn)
            range.append(mx-mn)
        ans = 0
        for i, num in enumerate(nums):
            if range[i] == mx_range:
                ans+=num
        return ans