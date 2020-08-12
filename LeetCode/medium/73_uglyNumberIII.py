# https://leetcode.com/problems/ugly-number-iii/
# https://leetcode.com/problems/ugly-number-iii/discuss/719717/Python-Binary-SearchMath.-Easy-Understand
# https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems

# Total number of multiple on a=2, b=3, c=5, from 1 to k = 50
# = ( k // 2 + k // 3 + k // 5 ) - ( k // lcm(2,3) - k // lcm(2, 5) - k // lcm(3, 5) ) + k // lcm( 2, 3, 5 )
# = 50 // 2 + 50 // 3 + 50 // 5 - 50 // 6 - 50 // 10 - 50 // 15 + 50 // 30
# = #Mutiple of 2 + #Multiple of 3 + #Multiple of 5 - #Multiple of 6 - #Multiple of 10 - #Multiple of 15+ #Multiple of 30
# = 25 + 16 + 10 - 8 - 5 - 3 + 1

import math

def nthUglyNumber(n, a, b, c):
    
    def enough(num):
        total = mid//a + mid//b + mid//c - mid//ab - mid//ac - mid//bc + mid//abc
        return total >= n

    ab = a * b // math.gcd(a, b)
    ac = a * c // math.gcd(a, c)
    bc = b * c // math.gcd(b, c)
    abc = a * bc // math.gcd(a, bc)

    left, right = 1, 10 ** 10
    while left < right:
        mid = left + (right - left) // 2
        if enough(mid):
            right = mid
        else:
            left = mid + 1
    return left


n = 3
a = 2
b = 3
c = 5
# Output: 4
print(nthUglyNumber(n, a, b, c))