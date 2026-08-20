# Problem: Starters 252- Skip one
# Problem Link: https://www.codechef.com/START252C/problems/SKIPONE
# cook your dish here
def solve():
    n,k = map(int, input().split())
    prices = [int(d) for d in input().split()]
    total = 0
    cnt = 0
    coupon = True
    target_index = 0
    mx_price = 0
    for i,price in enumerate(prices):
        if total+price>k:
            if price > mx_price:
                target_index=i
            break
        total += price
        if price>mx_price:
            target_index=i
            mx_price = price
            
   
        
    total=0
    for i,price in enumerate(prices):
        if i == target_index:
            cnt+=1
            continue
        if total+price>k:
            break
        total+=price
        cnt+=1
    print(cnt)