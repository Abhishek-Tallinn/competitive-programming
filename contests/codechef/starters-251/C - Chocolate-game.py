# Problem: Starters 251- Chocolate game
# Problem Link: https://www.codechef.com/problems/CHOCGM

# cook your dish here
def solve():
    n = int(input())
    boxes = [int(d) for d in input().split()]
    total = sum(boxes)
    remaining = total
    if remaining%2==0:
        alice_total = 0
        for chocolates in boxes:
            if chocolates%2==0:
                alice_total+=chocolates
                remaining-=chocolates
            else:
                alice_total+=(chocolates-1)
                remaining-=(chocolates-1)
        if remaining:
            alice_total+=(remaining+1)//2
        print(alice_total)
    else:
        bob_total = 0
        for chocolates in boxes:
            if chocolates%2==0:
                bob_total+=chocolates
                remaining-=chocolates
            else:
                bob_total+=chocolates-1
                remaining-=(chocolates-1)
        if remaining:
            bob_total+=(remaining+1)//2
        print(total-bob_total)