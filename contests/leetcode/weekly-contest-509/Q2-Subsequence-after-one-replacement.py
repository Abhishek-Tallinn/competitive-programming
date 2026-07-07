# Problem: Q2 - Subsequence after One Replacement
# Problem Link: https://leetcode.com/contest/weekly-contest-505/problems/subsequence-after-one-replacement/


class Solution:
    def canMakeSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        allowed = 1
        skipped = ''
        
        for j in range(len(t)):
            if t[j] == s[i]:
                i+=1 
            elif t[j]!=s[i] and allowed:
                allowed-=1
                skipped = s[i]
                i+=1
            elif t[j]!=s[i] and t[j] == skipped:
                allowed+=1
            
            if i == len(s):
                return True
        return i==len(s) 