
def power(x, y):
    result, power = 1.0, y
    print("result: ", bin(result))
    print("power: ", bin(power))
    print("")

    if y < 0:
        power, x = -power, 1.0 / x

    while power:
        print("power: ", bin(power))
        print("")
        if power & 1:
            result *= x
            print("result: ", bin(result))
            print("")

        x, power = x * x, power >> 1
        print("x: ", bin(x))
        print("power: ", bin(power))
        print("")

    return result


print(power(2, 2))
