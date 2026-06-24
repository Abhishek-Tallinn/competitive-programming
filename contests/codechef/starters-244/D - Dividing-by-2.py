# Problem: Starters 244- Dividing by 2
# Problem Link: https://www.codechef.com/START244D/problems/DIV2

# cook your dish here
def solve():
    def longest_common_prefix(strs):
        if not strs:
            return ""
        prefix = []
        for chars in zip(*strs):
            if len(set(chars))==1:
                prefix.append(chars[0])
            else:
                break
        return ''.join(prefix)
        
    n = int(input())
    arr = [int(d) for d in input().split()]
    arr.sort()
    bits = []
    for num in arr:
        bits.append(bin(num)[2:])
        final = longest_common_prefix(bits)
    cnt = 0
    for num in bits:
        cnt+=(len(num)-len(final))
    print(cnt)
        







t = int(input())
for _ in range(t):
    solve()