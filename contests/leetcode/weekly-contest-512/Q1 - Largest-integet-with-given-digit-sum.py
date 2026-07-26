# Problem: Q1 - Largest integer with given digit sum
# Problem Link: https://leetcode.com/problems/largest-integer-with-given-digit-sum/

class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        mx_int = int('9'*n)
        if s>9*n:
            return -1
        if s==0:
            return 0
        while mx_int>0:
            if sum([int(i) for i in (str(mx_int))]) == s:
                return mx_int
            mx_int-=1
        return -1