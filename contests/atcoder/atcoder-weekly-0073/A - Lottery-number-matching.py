# Problem: AWC 00732 A - Lottery Number matching
# Difficulty: 266 points(easy)
# Link: https://atcoder.jp/contests/awc0073/tasks/awc0073_a
# Time Complexity: O(n) where n is length of the ticket list
# Space Complexity: O(n) as we convert winning number into a set
# Approach: We iterate over tickets and check if they are in winning number. To ensure O(1) loop up we convert winning numbers into a set.


k , m = map(int,input().split())
winning_numbers = [int(d) for d in input().split()]
tickets = [int(x) for x in input().split()]

winning_numbers = set(winning_numbers)
cnt = 0
for ticket in tickets:
  if ticket in winning_numbers:
    cnt+=1
  
print(cnt)