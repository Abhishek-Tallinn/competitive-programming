# cook your dish here
# Problem: Starters 253- Flower reversal
# Problem Link: https://www.codechef.com/START253C/problems/FLREV
def solve():
    n = int(input())
    s = input()
    runs = []
    for ch in s:
        if runs and runs[-1][0] == ch:
            runs[-1][1]+=1
        else:
            runs.append([ch,1])
    
    beauty = 0
    for i in range(len(s)-1):
        if s[i]==s[i+1]:
            beauty+=1
    
    if len(runs)==1 or len(runs)==2:
        print(beauty)
        return
    if len(runs)==3:
        print(beauty+1)
        return
    
    print(beauty+2)




t = int(input())
for _ in range(t):
    solve()