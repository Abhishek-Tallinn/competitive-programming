# Problem: DSA Monday 013 -  Array Compression
# Problem Link: https://www.codechef.com/DSAMONDAY013/problems/ARCO

# cook your dish here
n = int(input())
arr = [int(d) for d in input().split()]
repeat = 0
i = 0
while i< len(arr)-1:
    while i+1<len(arr) and arr[i]==arr[i+1]:
        repeat+=1
        i+=1
    i+=1
print(len(arr)-repeat)
    
