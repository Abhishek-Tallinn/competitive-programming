# cook your dish here
# Problem: Starters 253- Monochrome cut
# Problem Link: https://www.codechef.com/START253c/problems/CIRCUT
def solve():
    n = int(input())
    a = [int(d) for d in input().split()]
    s = input()
    
    maxs = []
    curmx = a[0]
    for i in range(1, n):
        if s[i] == s[i-1]:
            curmx = max(curmx, a[i])
        else:
            maxs.append(curmx)
            curmx = a[i]
    if s[0] == s[-1]:
        maxs[0] = max(maxs[0],curmx)
    else:
        maxs.append(curmx)
    print(maxs)
    maxs.sort(reverse=True)
    print(maxs[0]+maxs[1])