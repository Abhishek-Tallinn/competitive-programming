# Problem: Q2 - Aggregate two time series
# Problem Link: https://leetcode.com/problems/aggregate-two-time-series/


class Solution:
    def aggregateTimeSeries(self, series1: list[list[int]], series2: list[list[int]]) -> list[list[int]]:
        ans = []
        i = len(series1)-1
        j = len(series2)-1
        next1 = next2 = 0
        while i>=0 or j>=0:
            t1 = series1[i][0] if i>=0 else float('-inf')
            t2 = series2[j][0] if j>=0 else float('-inf')
            if t1>t2:
                next1 = series1[i][1]
                curr_time = t1
                i-=1
                ans.append([curr_time,next1+next2])
            elif t2>t1:
                next2 = series2[j][1]
                curr_time = t2
                j-=1
                ans.append([curr_time,next1+next2])
            else:
                next1 = series1[i][1]
                next2 = series2[j][1]
                curr_time = t1
                i-=1
                j-=1
                ans.append([curr_time,next1+next2])
        ans = ans[::-1]
        return ans