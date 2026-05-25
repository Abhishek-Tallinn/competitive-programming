# Problem: DSA Monday - Minimum distance between two nodes
# Problem Link: https://www.codechef.com/problems/CHEFDIST

from collections import deque
class Solution:
    def getMinimumDistance(self, n, edges, x, y):
        
        def bfs(start,target,visited,graph):
            #since no recursive calls how can i have it here
            q = deque([start])
            visited[start] = True
            d = [0]*(n+1) #keep distance array
            while q:
                node = q.popleft()
                if node==target:
                    return d[node]
                for neighbour in graph[node]:
                    if not visited[neighbour]:
                        visited[neighbour] = True
                        d[neighbour]=1 + d[node]
                        q.append(neighbour)
                    
                    
            return -1 #no path
         
        graph = [[] for _ in range(n+1)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False]*(n+1)
        return bfs(x,y,visited,graph)