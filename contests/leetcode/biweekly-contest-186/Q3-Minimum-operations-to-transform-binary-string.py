# Problem: Q3 - Minimum operations to transform binary string
# Problem Link: https://leetcode.com/contest/biweekly-contest-186/problems/minimum-operations-to-transform-binary-string

class Solution:
    def minOperations(self, s1: str, s2: str) -> int:
        if s1==s2:
            return 0
        if len(s1)==1 and s1=='1':
            return -1
        ops = 0
        i = 0
        while i < len(s1):
            if s1[i]!=s2[i]:
                if s1[i]=='0':
                    ops+=1
                elif s1[i]=='1':
                    if i+1<len(s1) and s1[i+1]=='1' and s2[i+1]=='0':
                        ops+=1
                        i+=2
                        continue
                    else:
                        ops+=2
            i+=1
        return ops
        
    