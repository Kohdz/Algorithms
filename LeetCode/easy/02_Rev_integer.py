# Reverse Integer
# Given a 32-bit signed integer, reverse digits of an Integer
# 32-bit signed interger range [-2^31, 2^31-1]; return - if overflow

# Example:
#     Input: 123
#     Output: 321
    
#     Input: -123
#     Output-321
    
#     Input: 120
#     Output: 21

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
         


def reverse(x):
    s_nums = Stack()
    s_sign = Stack()

    rev = ''
    
    if x < 0:
        s_sign.push('-')
        x = x * -1

    while x >  0:
        mod = x % 10
        rev = rev + str(mod)
        x = x // 10

    
    lead_zero = False
    while not lead_zero:
        
        if rev[0]== '0':
            rev = rev[1:]
        else:
            lead_zero = True


    return(rev)

    if not s_sign.isEmpty():
        rev = str(s_sign.pop()) + rev

  

x = 1200
print(reverse(x))


def reverseHer(x):
    # -214784648 ~ 213783647
    num = 0

    # return the absolute value of a number
    a = abs(x)

    while(a! = 0)
        # 123 
        # a = 123
        # num = 0
        
        #first iteration
        # a = 12
        # num = 0

        #second iteration
        # a = 1
        # num = 32

        # third iteration
        # a = 0
        # num = 321

        temp = a % 10
        num = num * 10 + temp
        a = a // 10

    if x > 0 and num < 214784648:
        return num
    elif x < 0 and num <= 214784648
        return -num
    else:
        return 0


