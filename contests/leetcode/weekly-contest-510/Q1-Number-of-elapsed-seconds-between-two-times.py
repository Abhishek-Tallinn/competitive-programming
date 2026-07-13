# Problem: Q1 - Number of elapsed seconds between two times
# Problem Link: https://leetcode.com/problems/number-of-elapsed-seconds-between-two-times/


class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        start_h,start_m,start_s = map(int,startTime.split(':'))
        end_h,end_m,end_s = map(int,endTime.split(':'))
        h_diff = end_h - start_h
        if h_diff == 0 and end_m == start_m:
            return end_s-start_s
        if h_diff == 0:
            return (end_m-start_m)*60 - start_s + end_s
        if h_diff >=1:
            #if end_m == 0: end_m = 60
            s_bump = 60 - start_s    
            m_bump = 60 - (start_m + 1)
            start_h += 1
            h_diff = end_h - start_h 
            total = h_diff * 3600 + end_m * 60 + m_bump * 60 + s_bump + end_s
            return total