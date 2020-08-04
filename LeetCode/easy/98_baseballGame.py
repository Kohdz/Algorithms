# https://leetcode.com/problems/baseball-game/

def baseBallGame(operations):
    
    sum = 0
    last_valid = []
    
    
    for idx, str in enumerate(operations):
        
        if str.isdigit() or str[1:].isdigit():
            sum += int(str)
            last_valid.append(int(str))
            
        elif str == "D":
            add = last_valid[-1]*2
            sum += add
            last_valid.append(add)
            
            
        elif str == "C":
            sum -= last_valid[-1]
            last_valid.pop()
            
        else:
            add = last_valid[-1] + last_valid[-2]
            sum += add
            last_valid.append(add)            
    return sum
                

operations = ["5","-2","4","C","D","9","+","+"]
# Output: 27
print(baseBallGame(operations))