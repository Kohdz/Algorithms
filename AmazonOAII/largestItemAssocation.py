
from collections import defaultdict


from collections import deque, defaultdict

def largest_item_association(item_association):
    
    graph = defaultdict(set)
    
    for item1, item2 in item_association:
        graph[item1].add(item2)
        graph[item2].add(item1)
    
    largest_group = []
    visited = set()

    for key in graph.keys():
        
        if key not in visited:
            curr_group = []
            
            queue = deque()
            queue.append(key)
            while queue:
                currItem = queue.popleft()
                visited.add(currItem)
                curr_group.append(currItem)
                for neighbor in graph[currItem]:
                    if neighbor not in visited:
                        queue.append(neighbor)
            if len(curr_group) > len(largest_group):
                largest_group = curr_group
     
    largest_group.sort()
    return largest_group

print(largest_item_association([['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5']]))
print(largest_item_association([['item1', 'item2'], ['item4', 'item5'], ['item3', 'item4'], ["item1","item4"]]))

# def LargestItemAssociation(items):

#     graph = defaultdict(list)

#     for u, v in items:
#         graph[u].append(v)
#         graph[v].append(u)

#     maxGroup = max(graph.values())

#     output = []
#     output.append(maxGroup[0])
#     print(output)

#     output.extend(graph[maxGroup[0]])

#     return sorted(output)

# items = [['item1', 'item2'], ['item3', 'item4'], ['item4', 'item5']]
# print(LargestItemAssociation(items))

# output : [item3, item4, item5]
#  there are two item association groups
# group1: [item1, item2]
# group2: [item3, item4, item5]




