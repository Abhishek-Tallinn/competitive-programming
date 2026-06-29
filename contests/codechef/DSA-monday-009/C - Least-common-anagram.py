# Problem: DSA Monday 009 - Least common anagram
# Problem Link: https://www.codechef.com/DSAMONDAY009/problems/SUBTWO

# cook your dish here
from collections import Counter

n = int(input())
strs = []
for _ in range(n):
    s = input()
    strs.append(s)
#print(strs)

first = Counter(strs[0])
ans = []
for char,freq in first.items():
    isCommon = True
    mn = freq
    for s in strs[1:]:
        if char not in s:
            isCommon = False
            break
        mn = min(mn,s.count(char))
    if isCommon:
        ans.extend(char*mn)
if not ans:
    print("no such string")
ans.sort()
print(''.join(ans))