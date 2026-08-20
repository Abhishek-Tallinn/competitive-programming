# Problem: DSA Monday 016 -  Chef and groups
# Problem Link: https://www.codechef.com/DSAMONDAY016/problems/GROFR
# cook your dish here
def solve():
    n = int(input())
    s = input()
    groups=0
    inGroup = False
    for seat in s:
        if seat=='0':
            inGroup=False
        if seat=='1' and inGroup:
            continue
        if not inGroup and seat=='1':
            inGroup=True
            groups+=1
        
    print(groups)