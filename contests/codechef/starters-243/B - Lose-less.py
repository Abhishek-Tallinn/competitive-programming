# Problem: Starters 243 - Lose less
# Problem Link: https://www.codechef.com/START243D/problems/LOSELESS

# cook your dish here
def solve():
    matches,points = map(int,input().split())
    wins = draws = 0
    if points==matches:
        print(0)
        return
    if points==0:
        print(matches)
        return
    if points<matches:
        print(matches-points)
        return
    if points>matches:
        total_wins = 0
        while (points-3*total_wins) > (matches-total_wins):
            total_wins+=1
        draws = points - (3*total_wins)
        losses = matches - (total_wins+draws)
        print(losses)