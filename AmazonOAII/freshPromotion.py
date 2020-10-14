# My solution using two pointers: https://leetcode.com/playground/CUnMJbjd

# codeIndex: index of current element in codeList
# matchFromIndex: index of a match for codeList[codeIndex] in shoppingCart
# For each codeIndex, we will find a match starting from matchFromIndex

# If we can find a match: move on to finding match for codeIndex+1 starting from matchFromIndex + k, with k is length of codeList[codeIndex]
# If we can not find a match: try to find a match for codeIndex starting from matchFromIndex + 1

def checkWinPrize(codeList, shoppingCart):
    if not codeList:
        return 1
    if not shoppingCart:
        return 0
    
    codeIndex = 0
    matchFromIndex = 0
    while codeIndex < len(codeList) and matchFromIndex + len(codeList[codeIndex]) <= len(shoppingCart):
        matched = True
        codes = codeList[codeIndex]
        for i in range(len(codes)):
            if codes[i] != 'anything' and codes[i] != shoppingCart[matchFromIndex+i]:
                matched = False
                break
        if matched:
            matchFromIndex = matchFromIndex + len(codes)
            codeIndex += 1
        else:
            matchFromIndex += 1
    
    return 1 if codeIndex == len(codeList) else 0


# Solved it with
# dfs() + memo()
# it should pass all the test cases, time-complexity: O((m*k)^n) m=len(shoppingcart), k = len(codeList[i]), n = len(codeList)
# In the same logic, BFS() should also work too. The time complexity might be high, so far I don't have better solutions

def check(secrets, purchase):
    if not secrets: return 1
    memo = {}

    def dfs(i, j, anything):
        if i >= len(secrets):
            return True
        elif j + len(secrets[i])-1 >= len(purchase):
            return False
        if (i, j, anything) in memo: 
            print("memo:", memo)
            return memo[(i, j, anything)]
        k = 0
        for jj in range(j, len(purchase)):
            if purchase[jj] == secrets[i][k] or ((not anything or purchase[jj] == anything) and secrets[i][k] == "anything"):
                tmp_anything = anything
                kk = k
                while jj+kk < len(purchase) and kk < len(secrets[i]):
                    if purchase[jj+kk] == secrets[i][kk] or ((not tmp_anything or purchase[jj+kk] == tmp_anything) and secrets[i][kk] == "anything"):
                        if not tmp_anything and secrets[i][kk] == "anything":
                            tmp_anything = purchase[jj+kk]
                        kk += 1
                    else:
                        break
                if kk == len(secrets[i]):
                    if dfs(i+1, jj+kk, tmp_anything):
                        memo[(i, j, anything)] = True
                        return True
        memo[(i, j, anything)] = False
        return False
    
    return dfs(0, 0, "")


input = [
    [[['apple', 'apple'], ['banana', 'anything', 'banana']], ['orange', 'apple', 'apple', 'banana', 'orange', 'banana']],
    [[['apple', 'apple'], ['banana', 'anything', 'banana']], ['banana', 'orange', 'banana', 'apple', 'apple']],
    [[['apple', 'apple'], ['banana', 'anything', 'banana']], ['apple', 'banana', 'apple', 'banana', 'orange', 'banana']],
    [[['apple', 'apple'], ['apple', 'apple', 'banana']], ['apple', 'apple', 'apple', 'banana']],
    [[['apple', 'apple'], ['banana', 'anything', 'banana']], ['orange', 'apple', 'apple', 'apple', 'apple', 'banana', 'orange', 'banana']],
    [[], ['apple', 'orange']],
    [[['apple', 'orange']], []],
    [[['apple', 'apple'], ['banana', 'anything', 'banana']], ['apple', 'apple', 'banana', 'banana']],
    [[['apple', 'apple'], ['apple', 'anything', 'banana']], ['apple', 'apple', 'banana', 'banana']],
    [[['apple', 'apple'], ['apple', 'anything', 'banana']], ['apple', 'apple', 'apple', 'apple', 'banana']],
    [[['apple', 'apple'], ['apple', 'banana']], ['apple', 'apple', 'apple', 'banana']],
    [[["anything", "apple" ], ["banana", "anything", "banana"]], ["orange", "grapes", "apple", "orange", "orange", "banana", "apple", "banana", "banana"]]
]

output = [
    1,
    0,
    0,
    0,
    1,
    1,
    0,
    0,
    0,
    1,
    1,
    1
]

for i in range(0, len(input)):
    print("Testcase {}: {}".format(i, "Passed" if checkWinPrize(input[i][0], input[i][1]) == output[i] else "Failed"))