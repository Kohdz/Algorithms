# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

def minAddToMakeValid(S):
    # Time | Space
    '''
    - if the current bracket is ) there has to be a previous opening bracket (
    - for the sequence to be balanced. If not then increment the counter unbalanced
    - if the current bracket is (, add it to the top of stack
    - in the end when you finish traversing the sequence, return len(stack) + unbalanced
    - len(stack) = brackets which were opened but not closed
    '''

    result, stack = 0, []
    
    for symbol in S:
        if symbol == "(":
            stack.append(symbol)
        elif stack:
            stack.pop()
        else:
            result += 1
        
    return result + len(stack)

S = "())"
# Output: 1

print(minAddToMakeValid(S))