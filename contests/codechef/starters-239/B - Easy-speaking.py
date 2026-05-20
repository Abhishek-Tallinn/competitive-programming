# Problem: Starters 239  - Easy speaking
# Problem Link: https://www.codechef.com/problems/EZSPK?tab=statement

def solve():
    n = int(input())
    s = input()
    consonant_count = 0
    vowels = {'a','e','i','o','u'}
    for char in s:
        if char not in vowels:
            consonant_count+=1
            if consonant_count>=4:
                print("Yes")
                return
        else:
            consonant_count=0
            
    print("No")
