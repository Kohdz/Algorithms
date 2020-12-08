def max_supply_profit_map(num_suppliers, inventory, order):
    profit = dict()
    for price in inventory:
        profit[price] = profit.get(price, 0) + 1
    
    curr_max = max(profit.items(), key=lambda x: x[0])[0]
    
    ret = 0       
    while order > 0:
        maxi = min(order, profit[curr_max])
        ret += curr_max*maxi
        order -= maxi
        profit[curr_max] -= maxi
        profit[curr_max-1] = profit.get(curr_max-1, 0) + maxi
        if profit[curr_max] == 0:
            del profit[curr_max]
            curr_max -= 1       

    return ret

def max_supply_profit_map_II(num_suppliers, inventory, order):

    result = 0

    # Key: inventory item - Value: frequency of this item
    hashMap = dict()
    maxItem = 0

    # Fill dictionary and get max item to start with.
    for item in inventory:
        maxItem = max(maxItem, item)

        if item not in hashMap:
            hashMap[item] = 0
        hashMap[item] += 1

    # Fetch items as long there is orders remaining
    while order > 0:

        order -= 1

        # Add current item profit
        result += maxItem

        # Decrease item frequency in the dictionary 
        hashMap[maxItem] -= 1
        nextMax = maxItem - 1
        
        # Add the next possible max profit(maxItem - 1) to the dictionary
        if nextMax in hashMap:
            hashMap[nextMax] += 1
        else:
            hashMap[nextMax] = 1

        # Only leave current maxItem if we exhausted all it's occurrences 
        if hashMap[maxItem] == 0:
            maxItem -= 1

    return result


import heapq
def maxSupplyHeap(num_suppliers, inventory, order):

    heap = []
    maxSum = 0

    for items in inventory:
        heapq.heappush(heap, -items)

    while order > 0 and heap:
        val = -heapq.heappop(heap)
        print('heap val', val)
        maxSum += val
        order -= 1
        heapq.heappush(heap, -val+1)
    
    return maxSum
    



print(max_supply_profit_map_II(2, [3, 5], 6))

# print(max_supply_profit_map(2, [2,5], 4))