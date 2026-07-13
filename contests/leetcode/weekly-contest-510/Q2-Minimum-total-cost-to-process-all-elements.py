# Problem: Q2 - Minimum total cost to process all elements
# Problem Link: https://leetcode.com/problems/minimum-total-cost-to-process-all-elements/description/


class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        MODULO = 10**9+7
        resource = k
        total =0
        for i in range(len(nums)):
            if (nums[i] > resource):
                ops_req = (nums[i]-resource+k-1)//k 
                resource+=k*ops_req
                total += ops_req
            resource -= nums[i]
        return (total*(total+1))//2%MODULO
            