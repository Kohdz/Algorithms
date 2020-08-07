

def StringShifts(s, shifts):
    
    move_left = 0
    lenght_of_string = len(s)
    
    for direction, amount in shifts:
        if direction == 0:
            move_left += amount
        else:
            move_left -= amount

    move_left %= lenght_of_string
    
    return s[move_left:] + s[:move_left]

s = "abc"
shift = [[0,1],[1,2]]

s2 = "abcdefg"
# efgabcd
shift2 = [[1,1],[1,1],[0,2],[1,3]]

print(StringShifts(s, shift) == 'abc')
print(StringShifts(s2, shift2) == 'efgabcd')