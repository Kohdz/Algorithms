# re


# def num(n):

#     print(n)
#     if n == 0:
#         return print("liftOff")
#     return num(n-1)


# n = 10
# num(n)


# def arrSum(arr):
#     sum = 0
#     for i in range(len(arr)):
#         print(arr[i])
#         if arr[i].isdigit():
#             sum += arr[i]
#         else:
#             sum += arrSum(arr[i])


# arr = [1, [2, 3, [4]]]  # 10
# print(arrSum(arr))


# def getSum(piece):
#     if len(piece) == 0:
#         return 0
#     else:
#         return piece[0] + getSum(piece[1:])


# arr = [1, 3, 4, 2, 5]
# print(getSum(arr))


# string = "hello"
# # return 2 vowels


# def countVowels(str):
#     vowels = 'aeiou'
#     counter = 0
#     if len(str) == 0:
#         return 0
#     if str[0] in vowels:
#         return 1 + countVowels(str[1:])
#     else:
#         return countVowels(str[1:])


# def reverseArray(arr, idx=1, newArr=[]):
#     if len(arr) - idx < 0:
#         return newArr

#     newArr.append(arr[len(arr)-idx])
#     return reverseArray(arr, idx+1, newArr)


# arr = [1, 2, 3, 4, 5]
# print(reverseArray(arr))


systems = {
    "power": {
        "batteries": True,
        "solarCells": True,
        "generator": True,
        "fuelCells": True
    },
    "telecoms": {
        "antennas": {
            "highGain": True,
            "mediumGain": True,
            "lowGain": True
        },
        "transmitter": True,
        "receiver": True
    },
    "attitudeControl": {
        "stabilization": {
            "spin": True,
            "threeAxis": True
        }
    },
    "propulsion": {
        "engines": {
            "engine1": True,
            "engine2": True,
            "engine3": False
        },
        "thrusters": True,
        "propellant": True
    },
    "environment": {
        "cooling": True,
        "heating": True,
        "lifeSupport": True
    }
}


# def allSystemsGo(obj):

#     # base case
#     # if its not empty you went through every boolean and its true
#     # if you reached a flase value then return false
#        for i in obj:
#             subsystems = obj[i]
#             if subsystems == False:
#                 return False
#             else:
#                 if allSystemsGo(subsystems):
#                     return False

#         return True

# print(allSystemsGo(systems))

# family = {
#     'Beverly Marquez': {
#         'Nina Rhone': {
#             'William Rhodes': None,
#             'Paul Nell': None,
#             'Sir Paddington the Fourth, of the county Wilstonshire': None
#         }
#     }
# }
def getLonestName(obj, longestName = ""):
    for i in obj:
        if len(i) > len(longestName):
            longestName = i
    
        if obj[i] != None:
            name = getLonestName(f)