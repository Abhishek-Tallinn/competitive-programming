# Problem: DSA Monday - Number of Islands 2
# Problem Link: https://www.codechef.com/problems/NUMISLAND2

class Solution:
    def numOfIslands(self, n: int, m: int, operators: list[list[int]]) -> list[int]:
        
        def calculateIslands(self,grid):
            if not grid:
                return 0
            
            rows = len(grid)
            cols = len(grid[0])
            visited = [[False] * cols for _ in range(rows)]
            
            def dfs(r,c):
                if(r<0 or c<0 or r>=rows or c>= cols or grid[r][c]==0 or visited[r][c]):
                    return
                visited[r][c] = True
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            islands = 0
            
            for r in range(rows):
                for c in range(cols):
                    if grid[r][c] == 1 and not visited[r][c]:
                        islands+=1
                        dfs(r,c)
            return islands
            
            
        ans = []
        # Your code goes here
        matrix = [[0 for _ in range(m)] for _ in range(n)]
        for r,c in operators:
            matrix[r][c] = 1
            res = calculateIslands(self,matrix)
            ans.append(res)
            
        return ans