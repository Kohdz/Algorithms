def findRadius(houses, heaters):

    houses.sort()
    heaters.sort()
    radius = 0
    i = 0

    for house in houses:
        print("len(heaters)): ", len(heaters))
        print("len(heaters[i])): ", heaters[i])
        print("house: ", house)
        while i < len(heaters) and heaters[i] < house:
            i += 1
        if i == 0:
            print("radius: ", radius)
            print("heaters[i]: ", heaters[i])
            print("house: ", house)
            radius = max((radius), heaters[i], house)
        elif i == len(heaters):
            print("radius: ", radius)
            print("house[-1]", house[-1])
            print("heaters[-1]: ", heaters[-1])
            return max(radius, house[-1], heaters[-1])
        else:
            print("heaters[i]-house: ", heaters[i]-house)
            print("house", house)
            print("house-heaters[i-1]: ", house-heaters[i-1])
            radius = max(radius, min(heaters[i]-house, house-heaters[i-1]))

        return radius


houses = [1, 2, 3, 4]
heaters = [1, 4]
# rad = 1
print(findRadius(houses, heaters))
