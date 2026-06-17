# Problem: Starters 243 - Starved for seating
# Problem Link: https://www.codechef.com/START243D/problems/STRSEAT

# cook your dish here
def solve():
    teams,seats = map(int,input().split())
    arr = [int(d) for d in input().split()]
    total_people = sum(arr)
    cnt = 0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if j==i:
                continue
            curr_people = total_people//2 + (arr[i]//2) + (arr[j]//2)
            if curr_people > seats:
                cnt+=1
    print(cnt)