# Problem: DSA Monday - Win the league
# Problem Link: https://www.codechef.com/problems/WINLEAGUE


def findLeagueWinner(A, M):
    # write your code here 
    if A>M:
        return "TEAM A"
    elif A<M:
        return "TEAM M"
    else:
        return "DRAW"
