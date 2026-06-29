# cook your dish here
# Problem: DSA Monday 009 - Rotting apples
# Problem Link: https://www.codechef.com/DSAMONDAY009/problems/MATROTAPPLE

from collections import deque
n,m = map(int,input().split())
grid = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    grid[i] = list(map(int,input().split()))

fresh_apples = 0
q = deque()

for row in range(n):
    for col in range(m):
        if grid[row][col]== 2:
            q.append((row,col))
        elif grid[row][col]==1:
            fresh_apples+=1
time_elapsed = 0

directions = [(-1,0),(0,1),(1,0),(0,-1)]

while q and fresh_apples>0:
    time_elapsed+=1
    current_level = len(q)
    for _ in range(current_level):
        curr_row,curr_col = q.popleft()
        for rd,cd in directions:
            next_row = curr_row+rd
            next_col = curr_col+cd
            if (0<=next_row<n) and (0<=next_col<m) and grid[next_row][next_col]==1:
                grid[next_row][next_col]=2
                q.append((next_row,next_col))
                fresh_apples-=1
                
if fresh_apples>0:
    print(-1)
else:
    print(time_elapsed)