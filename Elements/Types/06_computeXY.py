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





def multiplyII(x, y):


    # & - only shows positions that need to carry (helps us discover its location)
    # << - carry only gets applied 1 place left of where it was discovered (shift is dont on the carry)
    # ^ - simulates addition
        # - 0 + 0 = 0
        # - 1 + 0 = 1
        # - 0 + 1 = 1
        # - 1 + 1 = 0 ( remember in base 2, 1 + 1 = 2 and 2 = (10)). this zero is then carried
    def add(a, b):

        running_sum, carryin, k, temp_a, temp_b = 0, 0, 1, a, b
        # [k] is the bit we're looking at.

        while temp_a or temp_b:

            # [ak] and [bk] are the values of k-th bit of a and b
            ak, bk = (a & k), (b & k)
            
            # carry for the next digit will be 1, if at least two out of previous ak, bk, or previous carry (carryin)
            # is 1. Hence, carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
            carryout = (ak ^ bk)  | (ak ^ carryin) | (bk ^ carryin)
            
            # n k-th digit, we get 1 if odd number of ak, bk, or carryin is 1. Hence, ak ^ bk ^ 
            # carryin. Since we're getting only one bit, we can add it to running_sum by applying OR.
            running_sum |= ak ^ bk ^ carryin

            carryin, k, temp_a, temp_b = (carryin << 1), (k << 1), (temp_a >> 1), (temp_b >> 1)

            # finally, when a and b are exhausted (we reached their most significant bits), we still need to 
            # take care of potentially remaining carry flag. Thus, running_sum | carryin.
        return running_sum | carryin


    # have a running_sum
    running_sum = 0

    # loop through x:
    while x:
        # if meet condition add:
        if x & 1:
            running_sum = add(running_sum, y)
        
        x, y = (x >> 1), (y << 1)



    return running_sum
