# Problem: DSA Monday 012 -  Group Formation
# Problem Link: https://www.codechef.com/DSAMONDAY012/problems/CONN01

# cook your dish here
def solve():
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        u,v = map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False]*(n+1)
        
    def dfs(node):
        visited[node] = True
        size=1
        for nei in graph[node]:
            if not visited[nei]:
                size+=dfs(nei)
        return size
    count = 0 #count disconnected
    sizes = []
    for i in range(1,n+1):
        if not visited[i]:
            count += 1
            size = dfs(i)
            sizes.append(size)
    total = 1
    modulo = 10**9+7
    for size in sizes:
        total*=size
    print(count,total%modulo)
        



t = int(input())
for _ in range(t):
    solve()