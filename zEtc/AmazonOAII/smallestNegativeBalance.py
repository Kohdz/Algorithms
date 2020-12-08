# Smallest Negative Balance

# Time O(N) | Space O(N)

def smallest_negative_balance(balances):
    people = set()    
    for record in balances:
        people.add(record[0])
        people.add(record[1])
    
    balance = {person : 0 for person in people}

    # loop through and update everybody's balances
    for record in balances:
        balance[record[0]] -= record[2]
        balance[record[1]] += record[2]
    
    ret = []

    # i could just keep clearing the list and adding new people in one loop
    # but clearing list is O(n) op 
    smallest_balance = float('inf')
    for person, bal in balance.items():
        smallest_balance = min(smallest_balance, bal)
    
    if smallest_balance >= 0:
        return ["Nobody has a negative balance"]
    
    for person, bal in balance.items():
        if bal == smallest_balance:
            ret.append(person)
    
    # have to sort for ascending alphabetical order
    ret.sort()
    return ret


# Alex And Blake
balances = [['Alex', 'Blake', 2], ['Blake', 'Alex', 2],  ['Casey', 'Alex', 5], ['Blake', 'Casey', 7], ['Alex', 'Blake', 4], ['Alex', 'Casey', 4]]

# Nobody has a negative balance
balances2 = [["Alex", "Blake", 2], ["Blake", "Alex", 2],  ["Casey", "Alex", 5], ["Alex", "Casey", 5]]

# Blake
balances3 = [['Alex', 'Blake', 2], ['Blake', 'Alex', 2],  ['Casey', 'Alex', 5], ['Blake', 'Casey', 7], ['Alex', 'Blake', 4], ['Alex', 'Casey', 4], ["Casey", "Alex", 1]]

print(smallest_negative_balance(balances))
print(smallest_negative_balance(balances2))
print(smallest_negative_balance(balances3))
