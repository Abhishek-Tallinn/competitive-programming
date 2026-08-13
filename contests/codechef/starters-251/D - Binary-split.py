# Problem: Starters 251- Binary split
# Problem Link: https://www.codechef.com/problems/BINSPLT

# cook your dish here
def solve():
    n = int(input())
    s = input()
    seq = []
    for ch in s:
        if seq and seq[-1][0] == ch:
            seq[-1][1] += 1
        else:
            seq.append([ch,1])
    if len(seq) == 1:
        print(s)
        return
    best = None
    for i in range(len(seq)-1):
        (a,x), (b,y) = seq[i], seq[i+1]
        candidate = a*x + b*y
        if best is None or candidate<best:
            best = candidate
    print(best)