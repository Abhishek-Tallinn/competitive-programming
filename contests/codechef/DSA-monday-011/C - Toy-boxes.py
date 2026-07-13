# Problem: DSA Monday 011 -  Toy boxes
# Problem Link: https://www.codechef.com/DSAMONDAY011/problems/SHOPI


# cook your dish here
def solve():
    n,k = map(int,input().split())
    arr = [int(d) for d in input().split()]
    arr.sort()
    if k > len(arr)//2:
        large_box = sum(arr[-k:])
        small_box = sum(arr) - large_box
        print(large_box - small_box)
    else:
        small_box = sum(arr[0:k])
        large_box = sum(arr)-small_box
        print(large_box-small_box)




t = int(input())
for _ in range(t):
    solve()