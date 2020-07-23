# https://leetcode.com/problems/open-the-lock/

import collections

def openLock(deadends, target):
    

    if target == '0000':
        return 0
    
    visited = set(deadends)
    steps = 0
    queue = collections.deque()
    queue.append("0000")
    
    while queue:
        for _ in range(len(queue)):
            nums = queue.popleft()
            if nums == target:
                return steps
            
            if nums in visited:
                continue
            visited.add(nums)
            
            for idx in range(4):
                num = int(nums[idx])
                next_num = (num + 10 + 1) % 10
                prev_num = (num + 10 - 1) % 10
                
                queue.append(nums[:idx] + str(prev_num) + nums[idx + 1:])
                queue.append(nums[:idx] + str(next_num) + nums[idx + 1:])
        steps += 1
        
    return -1
    
target = "0202"
deadends = ["0201","0101","0102","1212","2002"]
# Output: 6
# Explanation:
# A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
# Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
# because the wheels of the lock become stuck after the display becomes the dead end "0102".

print(openLock(deadends, target))