# Problem: Starters 245- Triple threat
# Problem Link: https://www.codechef.com/problems/TRTR3 

# cook your dish here
def solve():
    n,x = map(int,input().split())
    ans = ['1']*n*3
    start = 0
    zeros = 3*n-x    
    for i in range(len(ans)):
        if zeros<=0:
            break
        j = i
        zeros_placed = 0
        while j<len(ans):
            if zeros>0 and ans[j]!='0':
                ans[j]='0'
                zeros-=1
                zeros_placed+=1
                if zeros==0:
                    break
                if zeros_placed==2:
                    break
            j+=n
            '''
             for i in range(n):
        if zeros >= 2:
            # Place two zeros in the current triplet to make f(A)[i] = 0
            res[i] = '0'
            res[i + n] = '0'
            zeros -= 2
        elif zeros == 1:
            # Place one zero, f(A)[i] will be 1
            res[i] = '0'
            zeros -= 1
        else:
            # No more zeros, f(A)[i] will be 1
            break
            '''
        
        
        
    print(''.join(ans))
        
    
    




t = int(input())
for _ in range(t):
    solve()