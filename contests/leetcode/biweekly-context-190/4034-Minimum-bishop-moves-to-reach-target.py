# Problem: Leetcode 4034 - Minimum bishop moves to reach target
# Difficulty: Medium
# Link: https://leetcode.com/problems/minimum-bishop-moves-to-reach-target/description/
# Time Complexity: O(1) as we just do math
# Space Complexity: O(1) 
# Approach: we check if bishop has to reach a target which is on the same diagnonal or anti diagonal. If yes it just needs 1 move
# otherwise it can reach anywhere in 2 moves. Also we check for parity between source and taret as otherwise bishop cannot reach there.

from typing import List

class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        start_x,start_y = source
        end_x,end_y = target
        if (start_x+start_y)%2 != (end_x+end_y)%2:
            return -1
        #anti diag
        if start_x+start_y==end_x+end_y:
            return 1
        # diag
        if abs(start_x-end_x) == abs(start_y-end_y) and abs((start_x+start_y) - (end_x+end_y))%2==0:
            return 1
        return 2