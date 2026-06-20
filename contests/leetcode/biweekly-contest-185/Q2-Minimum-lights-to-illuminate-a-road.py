# Problem: Q2 - Minimum lights to illuminate a road
# Problem Link: https://leetcode.com/contest/biweekly-contest-185/problems/minimum-lights-to-illuminate-a-road/description


import math
class Solution:
    def minLights(self, lights: list[int]) -> int:
        intervals = []
        n = len(lights)
        for i in range(len(lights)):
            if lights[i]!=0:
                intervals.append([max(0,i-lights[i]), min((n-1),i+lights[i])])
        if not intervals:
            return (n+2)//3
        #merge intervals
        intervals.sort(key = lambda x:x[0])
        res = []
        mi,mx = intervals[0]
        for i in range(1,len(intervals)):
            start,end = intervals[i]
            if mx<start:
                res.append([mi,mx])
                mi = start
                mx = end
            else:
                mx = max(mx,intervals[i][1])
    
        res.append([mi,mx])
        
        final = [0]*n
        for r in res:
            start,end = r
            for j in range(start,end+1):
                if final[j]==0:
                    final[j]=1
        k = 0
        req = 0
        print(final)
        while k < len(final):
            if final[k]==0:
                cnt=0
                while k< len(final) and final[k]==0:
                    cnt+=1
                    k+=1
                req += (cnt+2)//3
            k+=1
        return req