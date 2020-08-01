# https://leetcode.com/problems/copy-list-with-random-pointer/
# https://www.youtube.com/watch?v=viKm998YxFc
# https://www.youtube.com/watch?v=OvpKeraoxW0

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):       
        # Time O(n) | Space O(n)
        
        hash_map = {}
        
        # create dummy node
        dummyHead = result = Node(0)
        
        current = head

        # create a copy of all the nodes
        # link the copeid nodes to each other
        # use hash_map to link copied nodes to orginal nodes
        while current:
            
            # create new node
            NewNode = Node(current.val)
            
            # map/link the old node to the new node
            hash_map[current]= NewNode
            
            # dummy node points to current node
            dummyHead.next = NewNode
            
            # move both current and dummy next
            dummyHead = dummyHead.next
            current = current.next
            
            
        current = head
        
        # link random pointers in the copied nodes
        while current:
            
            # get the copied nodes from out link/map
            copiedNode = hash_map[current]
            
            # get the random value
            random = current.random
           
            # if random exists, 
            if random is not None:
                
                # connect copied node to copied node
                copiedRandom = hash_map[random]
                copiedNode.random = copiedRandom
            else:
                # there is no random and set it to random
                copiedNode.random = None
            current = current.next
            
        return result.next
                
def copyRandomListII(head):

    node_hash = {}
    temp = head
    new_temp = Node(-1, None, None)
    new_head = new_temp

    while temp is not None:
        node_hash[temp] = Node(temp.val, None, None)
        new_temp.next = node_hash[temp]
        temp = temp.next
        new_temp = new_temp.next
    temp = head

    for key in node_hash:
        if key.random is not None:
            node_hash[key].random = node_hash[key.random]
    return new_head.next
