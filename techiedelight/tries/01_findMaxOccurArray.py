# https://www.techiedelight.com/find-maximum-occurring-word-given-set-strings/

# A class representing a Trie node:
class TrieNode:
    def __init__(self):

        # count and key will be set only for leaf nodes
        # key stores the string and count stores its frequency so far
        self.key = None
        self.count = 0

        # each node stores a dictionary to its child nodes
        self.character = {}


# Iterative function to insert a String in TrieNode
def insert(head, str):

    # start from root node
    curr = head

    for c in str:
        # go to next node and create a node if path doesn't exists
        curr = curr.character.setdefault(c, TrieNode())

    # store key and its count in leaf nodes
    curr.key = str
    curr.count += 1


# Function to perform pre-order traversal of given TrieNode
# and find word with maximum frequency
def preOrder(curr, key='', max_count=0):

    # return false if Trie is empty
    if curr is None:
        return key, max_count

    for v in curr.character.values():

        # leaf node have non-zero count
        if max_count < v.count:
            key = v.key
            max_count = v.count

        # recur for current node children
        key, max_count = preOrder(v, key, max_count)

    return key, max_count


if __name__ == '__main__':

    # given set of keys
    dict = [
        "code", "coder", 'tempy', "coding"
     
    ]

    # Insert all keys into a trie
    head = TrieNode()
    for word in dict:
        insert(head, word)

    # perform pre-order traversal of given Trie and find key
    # with maximum frequency
    key, count = preOrder(head)

    print("Word :", key)
    print("Count:", count)
