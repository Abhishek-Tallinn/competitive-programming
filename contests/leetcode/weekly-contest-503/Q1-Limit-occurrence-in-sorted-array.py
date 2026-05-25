# Problem: Q1 - Limit occurrence in sorted array
# Problem Link: https://leetcode.com/contest/weekly-contest-503/problems/limit-occurrences-in-sorted-array/

from collections import Counter
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        freq = Counter(nums)
        ans = []
        #rint(freq)
        for key,value in freq.items():
            if value>k:
                ans.extend([key]*k)
            else:
                ans.extend([key]*value)
        return ans