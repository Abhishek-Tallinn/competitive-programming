# Problem: Q1 - Exactly one consecutive set bits pair
# Problem Link: https://leetcode.com/contest/biweekly-contest-184/problems/exactly-one-consecutive-set-bits-pair/

class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        b = bin(n)[2:]
        cnt = 0
        for i in range(len(b)-1):
            if b[i]=='1' and b[i+1]=='1':
                cnt+=1
        return cnt==1
            
        