# https://leetcode.com/problems/heaters/

# Winter is coming! Your first job during the contest is to design a standard heater with
# fixed warm radius to warm all the houses.

# Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius
# of heaters so that all houses could be covered by those heaters.

# So, your input will be the positions of houses and heaters seperately, and your expected output will
# be the minimum radius standard of heaters.

# Note:

# Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
# Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
# As long as a house is in the heaters' warm radius range, it can be warmed.
# All the heaters follow your radius standard and the warm radius will the same.


# Example 1:

# Input: [1,2,3],[2]
# Output: 1
# Explanation: The only heater was placed in the position 2, and if we use the radius
#  1 standard, then all the houses can be warmed.

def findRadius(houses, heaters):

    houses.sort()
    heaters.sort()
    radius = 0
    i = 0

    for house in houses:
        while i < len(heaters) and heaters[i] < house:
            i += 1
        if i == 0:
            radius = max(radius, heaters[i], house)
        elif i == len(heaters):
            return max(radius, house[-1], heaters[-1])
        else:
            radius = max(radius, min(heaters[i]-house, house-heaters[i-1]))

        return radius


houses = [1, 2, 3, 4]
heaters = [1, 4]
# rad = 1
print(findRadius(houses, heaters))
