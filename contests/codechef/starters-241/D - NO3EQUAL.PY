# Problem: Starters 241 - No 3 Equal
# Problem Link: https://www.codechef.com/problems/NO3EQUAL


# cook your dish here
def solve():
    n = int(input())
    s = input()
    cnt = 0
    i = 0
    while i < len(s)-2:
    #for i in range(0,len(s)-2):
        if s[i] == s[i+1] and s[i+1] == s[i+2]:
            cnt+=1
            i+=3
        else:
            i+=1
    print(cnt)