# https://leetcode.com/problems/partition-labels/

def partitionLabels(S):

    last = {c: i for i, c in enumerate(S)}
    output = []
    max_idx = last_idx = 0
    
    for curr_idx, char in enumerate(S):
        
        max_idx = max(max_idx, last[char])
        
        if max_idx == curr_idx:
            output.append(curr_idx - last_idx + 1)
            last_idx = curr_idx + 1
    
    return output



S = "ababcbacadefegdehijhklij"
# Output: [9,7,8]
print(partitionLabels(S))





