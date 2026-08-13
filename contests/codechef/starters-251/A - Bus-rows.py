# Problem: Starters 251- Bus rows
# Problem Link: https://www.codechef.com/problems/BUSROW

# cook your dish here
def solve():
    n,m,x = map(int,input().split())
    row_number = (x+(m-1))//m
    print(min(row_number,n-row_number+1))


t = int(input())
for _ in range(t):
    solve()