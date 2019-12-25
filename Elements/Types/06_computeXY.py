def multiply(x, y):
    def add(a, b):
        print("a: ", bin(a))
        print("b: ", bin(b))
        running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
        while temp_a or temp_b:
            print("k: ", bin(k))
            print("carryin: ", bin(carryin))
            print("temp_a: ", bin(temp_a))
            print("tempb: ", bin(temp_b))
            print("")
            ak, bk = a & k, b & k
            print("ak: ", bin(ak))
            print("bk: ", bin(bk))
            print("ak & k: ", bin(ak & k))
            print("bk & k: ", bin(bk & k))
            print("")
            print("ak & bk: ", bin(ak & bk))
            print("ak & carryin: ", bin(ak & carryin))
            print("bk & carryin: ", bin(bk & carryin))
            print("")
            carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            print("ak ^ bk: ", bin(ak ^ bk))
            print("carryin: ", bin(carryin))
            running_sum |= ak ^ bk ^ carryin
            print("running_sum: ", bin(running_sum))
            print("")

            carryin, k, temp_a, temp_b = \
                (carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)
            print("carryout: ", bin(carryout))
            print("k: ", bin(k))
            print("temp_a: ", bin(temp_a))
            print("temp_b: ", bin(temp_b))
            print("")

        print("running_sum | carrying: ", bin(running_sum | carryin))
        return running_sum | carryin

    running_sum = 0
    while x:  # examines each bit of x
        print("x: ", bin(x))
        print("")
        if x & 1:
            print("x & 1: ", bin(x & 1))
            running_sum = add(running_sum, y)
        print("x: ", bin(x >> 1))
        print("y: ", bin(y << 1))
        print("")
        x, y = x >> 1, y << 1
    return running_sum


x = 3
y = 2
print(multiply(x, y))
