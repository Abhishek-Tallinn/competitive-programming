# Problem: Starters 252- Mirror Swap
# Problem Link: https://www.codechef.com/START252C/problems/MRSWAP

# cook your dish here
def solve():
    n = int(input())
    arr = [int(d) for d in input().split()]
    left = 0
    right = len(arr)-1
    while left<right:
        if arr[left] < arr[right]:
            arr[left],arr[right] = arr[right],arr[left]
        left+=1
        right-=1
    print(sum(arr[0:n]))
    