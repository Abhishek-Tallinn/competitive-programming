# Problem: Starters 239  - Magic mirror
# Problem Link: https://www.codechef.com/problems/MIRRIM?tab=statement

def solve():
    n = int(input())
    b_boxes = [int(d) for d in input().split()]
    left = 0 
    right = n-1
    while left<right:
        if abs(b_boxes[left]-b_boxes[left+1]) != abs(b_boxes[right]-b_boxes[right-1]):
            print("No")
            return
        left+=1
        right-=1
    print("Yes")