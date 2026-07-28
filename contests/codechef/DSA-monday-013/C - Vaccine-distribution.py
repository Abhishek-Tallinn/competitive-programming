# Problem: DSA Monday 013 -  Vaccine Distribution
# Problem Link: https://www.codechef.com/DSAMONDAY013/problems/VACDI

# cook your dish here
def solve():
    n = int(input())
    V = [int(d) for d in input().split()]
    P = [int(d) for d in input().split()]
    if max(P) > max(V):
        print("No")
        return
    
    V.sort()
    P.sort()
    isPossible = True
    for i in range(len(V)):
        if P[i]>=V[i]:
            isPossible = False
            break
            
    if isPossible:
        print("Yes")
    else:
        print("No")
    
solve()
