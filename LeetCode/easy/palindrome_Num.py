# Determine whether an integer is a palindrome. An integer is a palindrome when
# it reads the same backwords as fordwards

# example 1:
#     Input: 121
#     Output: True

# example 2:
#     Input: -121
#     Output: False
 
num1 = 121
num2 = -121
num3 = 199
 
def isPalindrome(num):
    if num < 0:
        return False
    num_abs = abs(num)
    print(num_abs)
    d = Dequeue()

    isPal = False

    num_list = []
    while num_abs > 0:
        mod = num_abs % 10
        num_abs = num_abs // 10
        d.FrontAdd(mod)
        num_list.append(mod)

    num_list_rev = num_list[::-1]

    if num_list == num_list_rev:
        isPal = True

    return isPal

print(isPalindrome(num1))

def isPalindromeHER(x):
    num = 0
    a = abs(x)

    while (a != 0):
        temp = a % 10
        num = num * 10 + temp
        a = a // 10

    if x >= 0 and x == num:
        return True
    else:
        return False


