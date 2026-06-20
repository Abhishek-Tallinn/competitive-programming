# Problem: Q1 - Create grid with exactly one path
# Problem Link: https://leetcode.com/contest/biweekly-contest-185/problems/create-grid-with-exactly-one-path/description

class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = [['#' for _ in range(n)] for _ in range(m)]
        #iterate first row
        for j in range(n):
            grid[0][j] = '.'
        # last column
        for i in range(m):
            grid[i][n-1] = '.'
        res = []
        for row in grid:
            res.append(''.join(row))
        return res
        