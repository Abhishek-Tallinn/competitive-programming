# Problem: AWC 00732 B - Flipping Cards
# Difficulty: 300 points(easy)
# Link: https://atcoder.jp/contests/awc0073/tasks/awc0073_b
# Time Complexity: O(n log n) where n is the number of cards as we iterate over the cards and also sort the difference list
# Space Complexity: O(n) as we store the differences
# Approach: We calculate the score for each card and the difference between flipping and not flipping. 
# We then sort the differences in descending order and flip the top k cards. Since K flips are necessary any negative flips will be automatically recorded.


n, k = map(int, input().split())

score = 0
diffs = []

for _ in range(n):

    front, back = map(int, input().split())

    score += front
    diffs.append(back - front)

diffs.sort(reverse=True)

print(score + sum(diffs[:k]))