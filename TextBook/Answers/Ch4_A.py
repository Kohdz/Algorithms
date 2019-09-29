#Recursive Summation
# nums = [1,3,5,7,9]

# def listsum(nums):
#     if len(nums) == 1:
#         return nums
#     else:
#         return nums[0] + nums(nums[1:0])


# recursively converting from integer to string
#how does this problem remember the previous values
# def toStr(n, base):
#     convertString = "0123456789ABCDEF"
#     if n < base:
#         return convertString[n]
#     else: 
#         return toStr(n / base, base) + convertString[n%base]



# recursion to print a string backwords
revStr1 = "hello"

def stringReversal(revStr):
    if len(revStr) == 1:
        return revStr[0]
    elif len(revStr) == 0:
        return ""
    else:
        return stringReversal(revStr[1:]) + revStr[0]


# print(stringReversal(revStr1))


pal1 = "kayak"
pal2 = "aibohphobia"
pal3 = "Live not on evil"
pal4 = "Reviled did i live, said i, as I did deliver"
pal5 = "Go hang a salami; i'm a lasagna hog"
pal6 = "Able was i ere i saw Elba"
pal7 = "Kanakanak - a town in Alaska"
pal8 = "Wassamassaw - a town in South Dakota"

def nonChar(nonCharList):
    palLower = nonCharList.lower()

    charList = ''
    letters = "abcdefghijklmnopqrstuvwxyz"
    for i in palLower:
        if i in letters:
            charList += i
        
    return charList

def isPal(pal):
    palSteril = nonChar(pal)
    revStr = stringReversal(palSteril)
    if palSteril == revStr:
        return True
    else:
        return False

print(isPal(pal1))

