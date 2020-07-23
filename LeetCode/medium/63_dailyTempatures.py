# https://leetcode.com/problems/daily-temperatures/
# https://www.youtube.com/watch?v=WGm4Kj3lhRI

def dailyTemperaturesNextArray(T):
    
    # Time O(NW), N = lenght of T, W = number of allowed values for T[i]
    # Space O(N + W), the size of the answer and next array
    
    
    nxt = [float('inf')] * 102
    ans = [0]* len(T)
    
    for i in reversed(range(len(T))):
        
        # use 102 so min(nxt[t]) has a defualt value
        warmer_index = min(nxt[t] for t in range(T[i] + 1, 102))
        
        if warmer_index < float('inf'):
            ans[i] = warmer_index - i
        nxt[T[i]] = i
    return ans


def dailyTemperaturesStack(T):
    
    '''
    We go backwords so we know the warmer days before hand
    we compare the current day to the temp in the stack
    if the current tempature is colder then the stack day
    we can pop it off
    we push the new day onto the stack
    
    If the stack tempature is warmer then the current tempature
    we calculate the next warmer day by subtracting days (index),
    e.g, day 6 by day 5
    
    that current day gets added to the stack
    if the stack has a colder day, we keep poping
    '''
    
    # Time O(N) | Space O(W); W = len of stack 
    output = [0] * len(T)
    
    #indexes from hottest to coldest
    stack = [] 
    
    for i in reversed(range(len(T))):
        while stack and T[i] >= T[stack[-1]]:
            stack.pop()
        if stack:
            output[i] = stack[-1] - i
        stack.append(i)
    return output

T = [73, 74, 75, 71, 69, 72, 76, 73]
# output [1, 1, 4, 2, 1, 1, 0, 0].

print(dailyTemperaturesStack(T))