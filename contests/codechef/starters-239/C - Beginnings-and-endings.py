# Problem: Starters 239  - Beginnings and endings
# Problem Link: https://www.codechef.com/problems/EQBEND?tab=statement

from collections import defaultdict
def solve():
    n = int(input())
    arr = [int(d) for d in input().split()]
    min_moves = float('inf')
    #already good array
    if arr[0]==arr[-1]:
        print(0)
        return
    #this means no repetition so we cant make it good. Dont need freq
    if len(set(arr))==len(arr):
        print(-1)
        return
    arr_map = defaultdict(list)
    for idx,num in enumerate(arr):
        arr_map[num].append(idx)
    #calculate moves
    for key,values in arr_map.items():
        moves = (values[0]-0) + (len(arr)-1-values[-1])
        min_moves = min(min_moves,moves)
    
    
    print(min_moves)