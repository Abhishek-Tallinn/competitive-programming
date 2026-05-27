# Problem: Starters 240  - Binary Smile
# Problem Link: https://www.codechef.com/problems/RVBS

def solve():
    n = int(input())
    A = input()
    B = input()
    if A == B:
        print(0)
        return
    if A.count('1') != B.count('1'):
        print(-1)
        return
    min_ops = 0
    posA_1 = [i for i,ch in enumerate(A) if ch=='1']
    posB_1 = [i for i,ch in enumerate(B) if ch=='1']
    for i in range(len(posA_1)):
        if posA_1[i]!=posB_1[i]:
            min_ops+=1
    print(min_ops)        
            