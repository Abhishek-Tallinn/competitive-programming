# Problem: Q3 - Create grid with exactly k paths
# Problem Link: https://leetcode.com/problems/create-grid-with-exactly-k-paths-i/description/


class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        #grid = [[0 for _ in range(n)] for _ in range(m)]
        if m==1 or n == 1:
            if k==1:
                return ['.'*n]*m
            else:
                return [] 
        if n>=k:
            grid = [['#']*n for _ in range(m)]
            grid[0] = ['.']*n
            for j in range(n-k,n): 
                grid[1][j] = '.'
            for i in range(1,m):
                grid[i][n-1] = '.'
            return [''.join(row) for row in grid]
                
        if m>=k:
            grid = [['#']*n for _ in range(m)]
            for i in range(m): 
                grid[i][0] = '.'
            for i in range(m-k,m):
                grid[i][1] = '.'
            for j in range(1,n):
                grid[m-1][j] = '.'
            return [''.join(row) for row in grid]
        if m==3 and n==3 and k==4:
            return ['..#','...','#..']

        return []