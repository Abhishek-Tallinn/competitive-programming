# Problem: Q1 - Unique middle element
# Problem Link: https://leetcode.com/contest/biweekly-contest-186/problems/unique-middle-element


class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        return nums.count(nums[len(nums)//2])==1