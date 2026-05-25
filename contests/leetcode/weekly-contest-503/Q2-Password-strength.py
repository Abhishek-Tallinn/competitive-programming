# Problem: Q2 - Password strength
# Problem Link: https://leetcode.com/contest/weekly-contest-503/problems/password-strength/

class Solution:
    def passwordStrength(self, password: str) -> int:
        strength = 0
        password = set(password)
        for char in password:
            if char.islower():
                strength+=1
            elif char.isupper():
                strength+=2
            elif char.isdigit():
                strength+=3
            elif char in {'!','@','#','$'}:
                strength+=5
        return strength
        