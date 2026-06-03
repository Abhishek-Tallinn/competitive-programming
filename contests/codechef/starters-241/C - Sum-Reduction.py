# Problem: Starters 241 - Sum Reduction
# Problem Link: https://www.codechef.com/problems/SUMREDUCTION

# cook your dish here
def solve():
    n = int(input())
    arr = [int(d) for d in input().split()]
    a_sum = sum(arr)
    arr.sort()
    ans = arr[0]
    for num in arr[1:]:
        if ans & num == 0:
            ans+=num
    if ans == a_sum:
        print("Yes")
        return
    print("No")
        