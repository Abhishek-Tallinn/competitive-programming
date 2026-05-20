# Problem: AWC 00732 C - Synergy at the Flea Market
# Difficulty: 366 points(medium)
# Link: https://atcoder.jp/contests/awc0073/tasks/awc0073_c
# Time Complexity: O(n) as we run the sliding window through the list and keep track of window_sum
# Space Complexity: O(n log n) as we store the inputs in points and also sort it
# Approach: We use a sliding window to track the pairs starting from left and moving towards right. With each new booth we keep incrementing the window sum with its attractiveness and before that
# we add into the total the product of current booth's attractiveness and the window sum. We also check if the current booth is out of range with the left pointer and if it is we keep moving the left pointer until it is in range 
# and also decrement the window sum with the attractiveness of the booth at left pointer.
    

n , d = map(int,input().split())
points = []
for _ in range(n):
  c,s = map(int,input().split())  
  points.append([c,s])

points.sort()
left = right = 0
total = 0
window_sum = 0
for right in range(n):
  
  c,s = points[right]
  
  while c - points[left][0]>d:
    window_sum-=points[left][1]
    left+=1
  total+= s*window_sum
  
  window_sum += s

print(total)
  