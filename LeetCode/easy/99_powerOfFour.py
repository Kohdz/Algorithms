# https://leetcode.com/problems/power-of-four/



def isPowerOfFourLog(num):
    
    # Time Log4(n) | Space O(1)
    # Check If Bits Were Lost
    # we right shift by 2 (neaning 4 bits)
    # then we left shift by the same amount
    # we then compare if it is equal to the number
    # we right shift untill the nunber becomes 1
    # if we dont get back the number, it was not a power of 4
    
    n = num
    count = 0
    
    if num < 1:
        return False
    
    while n > 1:
        n >>= 2
        count += 2
        
    return (n << count == num)


def isPowerOfFourBitCheck(n):

    # Time O(1) | Space O(1)

    # we know n & (n -1 ) == 0 for powers of two
    # infact we can use it to get the set bits
    # we also know that n % 3 == 1 for powers of 4 
    return (n > 0 and ((n & (n-1)) == 0) and (n % 3 == 1))

n = 16
print(isPowerOfFourBitCheck(n))