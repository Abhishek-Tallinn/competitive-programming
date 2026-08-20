# Problem: Starters 252- Odd even
# Problem Link: https://www.codechef.com/START252C/problems/ODDEVEN7
# cook your dish here
def solve():
    n = int(input())
    arr = [int(d) for d in input().split()]
    odd_cnt=even_cnt = 0
    for num in arr:
        if num%2==0:
            even_cnt+=1
        else:
            odd_cnt+=1
    if odd_cnt==len(arr)//2 or even_cnt==len(arr)//2:
        print(len(arr))
    elif odd_cnt<len(arr)//2:
        print(odd_cnt*2+1)
    elif even_cnt<len(arr)//2:
        print(even_cnt*2+1)
    