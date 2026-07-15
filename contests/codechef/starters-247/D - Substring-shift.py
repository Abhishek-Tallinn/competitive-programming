# Problem: Starters 246- Substring shift
# Problem Link: https://www.codechef.com/START247D/problems/STRINGSHIFT

def solve():
    n = int(input())
    s = input()
    z_idx = []
    z_found = False
    ans = ""
    for i in range(len(s)):
        if s[i]=='z':
            if z_idx and i != z_idx[-1]+1:
                break
            z_idx.append(i)
    if not z_idx:
        print(s)
        return
    ans = []
    for i in range(z_idx[0]):
        ans.append(s[i])
    for i in range(z_idx[0],z_idx[-1]+1):
        ans.append('a')
    for i in range(z_idx[-1]+1,len(s)):
        ans.append(s[i])
    print(''.join(ans))
        