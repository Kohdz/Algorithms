def packaging_automation(groups):
    groups.sort()
    groups[0]=1
    for i in range(1, len(groups)):
        if groups[i]-groups[i-1]>1:
            groups[i]=groups[i-1]+1
    return groups[-1]


def packingAutomationII(groups):

    n = len(groups)

    count = [0]* (n + 1)

    for i in groups:
        count[min(i, n)] += 1
    
    size = 0
    ans = 0
    # print(count)
    for i in range(n):

        while (count[i] > 0 and size < i):
            size += 1
            ans += size
            count[i] -= 1

        ans + (i*count[i])

    return ans

# print(f'{packaging_automation([1,3,2,2])} == 3')
# print(f'{packaging_automation([3,2,3,5])} == 4')
# print(f'{packaging_automation([3])} == 1')

print(f'{packingAutomationII([1,3,2,2])} == 3')
print(f'{packingAutomationII([3,2,3,5])} == 4')
print(f'{packingAutomationII([3])} == 1')