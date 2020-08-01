# https://www.techiedelight.com/lexicographic-sorting-given-set-of-keys/

class Trie:
    def __init__(self):

        self.key = None

        # Trie supports lower case english characters (a-z)
        # so character size is 26
        self.characters = [None] * 26

# Iterative function to insert a String in Trie
def insert(head, str):

    # start from root node
    curr = head

    for c in str:
        key = ord(c) - ord('a')

        # create a node if path doesn't exit
        if curr.character[key] is None:
            curr.character[key] = Trie()

        # go to next node
        curr = curr.character[key]
    
    # store key in leaf node
    curr.key = str

# Function to perform pre-order traversal of given Trie
def preorder(curr):


    # return false if Trie is empty
    if curr is None:
        return

    for i in range(26):
        if curr.characters[i]:

            # if leaf node, print key
            if curr.character[i].key:
                print(curr.character[i].key)

        preorder(curr.character[i])

dict = [
    "lexicographic", "sorting", "of", "a", "set", "of", "keys", "can", "be",
    "accomplished", "with", "a", "simple", "trie", "based", "algorithm",
    "we", "insert", "all", "keys", "in", "a", "trie", "output", "all",
    "keys", "in", "the", "trie", "by", "means", "of", "preorder",
    "traversal", "which", "results", "in", "output", "that", "is", "in",
    "lexicographically", "increasing", "order", "preorder", "traversal",
    "is", "a", "kind", "of", "depth", "first", "traversal"
]
 
head = Trie()

# insert all keys of dictionary into trie
for word in dict:
    insert(head, word)

# print keys in lexicographic order
preorder(head)