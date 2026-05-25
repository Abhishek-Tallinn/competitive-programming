# Problem: Q3 - Minimum operations to sort a permutation
# Problem Link: https://leetcode.com/contest/weekly-contest-503/problems/minimum-operations-to-sort-a-permutation/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        i = nums.index(0)
        n = len(nums)
        isReverse = False
        x = 0
        #basically check both parts first to confirm reverse
        for j in range(i,n):
            if nums[j]!=x:
                isReverse = True
                break
            x+=1
        if not isReverse:
            for k in range(i):
                if nums[k]!=x:
                    isReverse = True
                    break
                x+=1
        if isReverse:
            x=0
            #just cases to return -1
            for j in range(i,-1,-1):
                if nums[j]!=x:
                    return -1
                x+=1
            for j in range(n-1,i,-1):
                if nums[j]!=x:
                    return -1
                x+=1
            return min(1+(n-1-i),(i+1)%n + 1) #kind of like dp case here

        return min(i,1+(n-i)%n +1)
        