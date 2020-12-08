# Utilization Checks
# Autoscale Policy

def inalInstances(instances, averageUtil):

    # 25 < inst = half
    # 25 < inst < 60 = same
    # 60 > inst = double

    idx = 0
    count = instances
    LIMIT = 2 * 100_000_000
    while idx < len(averageUtil):
        print('idx', idx)
        print('count', count)

        if averageUtil[idx] < 25:
            
            print (f'entered if because *{averageUtil[idx]}* is smaller than 25')
            if count > 1:
                if count % 2 == 0:
                    count = count // 2 + 0
                else:
                    count = count // 2 + 1
                idx += 10
        elif averageUtil[idx] > 60:

            print (f'entered if because *{averageUtil[idx]}* is greater than 60')
            temp = 2 * count
            if temp <= LIMIT:
                count = temp
                idx += 10
        
        idx += 1

   
    return count


instances = 2
averageUtil = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 80]
# averageUtil = [25, 23, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 76]
print(inalInstances(instances, averageUtil))