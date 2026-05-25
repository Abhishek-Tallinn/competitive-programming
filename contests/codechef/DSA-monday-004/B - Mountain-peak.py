# Problem: DSA Monday - Mountain peak
# Problem Link: https://www.codechef.com/problems/DSCPPAS269P

def next_higher_peak(heights):
    # Write your code here
    ans = [-1]*len(heights)
    stack = []
    for i in range(len(heights)-1,-1,-1):
        while stack and stack[-1]<=heights[i]:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        stack.append(heights[i])
    return ans