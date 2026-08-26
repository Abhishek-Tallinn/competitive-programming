# Problem: Starters 253- Posh shopping
# Problem Link: https://www.codechef.com/START253C/problems/POSHOP
# cook your dish here
def solve():
    n = int(input())
    costs = [int(d) for d in input().split()]
    mx_single = max(costs)
    mx = 0
    for i in range(len(costs)):
        for j in range(i+1,len(costs)):
            if costs[j] >= costs[i]:
                mx = max(mx,costs[i]+costs[j])
    print(max(mx,mx_single))