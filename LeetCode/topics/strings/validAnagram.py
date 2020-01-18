# Given a string, determine if it is a palindrome,
#  considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:
# Input: "A man, a plan, a canal: Panama"
# Output: true

# Example 2:
# Input: "race a car"
# Output: false


class Dequeue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def frontAdd(self, elem):
        self.items.append(elem)

    def rearAdd(self, elem):
        self.items.insert(0, elem)

    def frontPop(self):
        return self.items.pop()

    def rearPop(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


s = "A man, a plan, a canal: Panama"
s1 = "race a car"


def isPalindrome(s):
    d = Dequeue()
    stel = Sterilizer(s)
    pal = True
    for i in stel:
        d.frontAdd(i)

    print(d.items)

    while d.size() > 1 and pal:
        first = d.frontPop()
        last = d.rearPop()
        if first != last:
            pal = False

    return pal


def Sterilizer(s):
    clean = ''
    let_nums = 'abcdefghijklmnopqrstuvwxyz0123456789'
    s_lower = s.lower()
    for i in s_lower:
        if i in let_nums:
            clean += i
    return clean


# print(isPalindrome(s))
print(isPalindrome(s1))


def isPalHer(s):

    i, j = 0, (len(s)-1)

    while i < j:
        while i < j and not s[i].isalnum():
            i += 1
        while i < j and not s[j].isalnum():
            j -= 1
        if s[i].lower() != s[j].lower():
            return False

        i += 1
        j -= 1
    return True
