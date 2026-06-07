# Problem: Q2 - Valid binary strings with cost limit
# Problem Link: https://leetcode.com/contest/weekly-contest-505/problems/valid-binary-strings-with-cost-limit/

class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:
        def is_valid(s,k):
            if '11' in s:
                return False
            cost = 0
            for i in range(len(s)):
                if s[i]=='1':
                    cost+=i
                    if cost>k:
                        return False
            return True
        res= []
        for i in range(2**n):
            temp= format(i, f'0{n}b')
            if is_valid(temp,k):
                res.append(temp)
        return res