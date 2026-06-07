# Problem: Q2 - Minimum energy to maintain brightness
# Problem Link: https://leetcode.com/contest/biweekly-contest-184/problems/minimum-energy-to-maintain-brightness/

class Solution:
    def minEnergy(self, n: int, brightness: int, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        #print(intervals)
        m_intervals = []
        mx = intervals[0][1]
        mn = intervals[0][0]
        for i in range(1,len(intervals)):
            if mx<intervals[i][0]: #break case
                m_intervals.append([mn,mx])
                mn = intervals[i][0]
            mx = max(mx,intervals[i][1])
        m_intervals.append([mn,mx])
        #print(m_intervals)
        # in this time we need to do something
        on_bulbs = (brightness+2)//3
        mn_total_energy = 0
        for i in range(len(m_intervals)):
            time = m_intervals[i][1] - m_intervals[i][0]+1
            mn_total_energy += on_bulbs*time
        return mn_total_energy