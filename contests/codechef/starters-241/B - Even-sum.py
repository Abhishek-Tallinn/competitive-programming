# Problem: Starters 241 - Even sum
# Problem Link: https://www.codechef.com/problems/EVENSUM1

# cook your dish here
def solve():
    n = int(input())
    arr = [int(d) for d in input().split()]
    a_sum = sum(arr)
    c_odd=c_even = 0
    for num in arr:
        if num%2==0:
            c_even+=1
        else:
            c_odd+=1
    if a_sum%2==0 and c_even>0:
        print("Yes")
        return
    if a_sum%2==1 and c_odd>0:
        print("Yes")
        return
    print("No")