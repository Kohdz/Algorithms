# https://www.techiedelight.com/longest-common-prefix-given-set-strings-using-trie/

class TrieNode:

    def __init__(self):

        self.characters = {}
        self.endOfWord = False


def insert(head, word):


    currNonde = head

    for char in word:
        if char not in currNonde.characters:
            currNonde.characters[char] = TrieNode()
        currNonde = currNonde.characters[char]
    currNonde.endOfWord = True

    # for c in word:
    #     currNonde = currNonde.characters.setdefault(c, TrieNode())
    # currNonde.endOfWord = True

def LCPPrefix(words):

    # insert all keys into trie
    head = TrieNode()
    for word in words:
        insert(head, word)

    # traverse the trie and find the longest common prefix
    lcp = ""
    curr = head

    # do till we find a leaf node or node has more than 1 children
    while curr and not curr.endOfWord and len(curr.characters)  == 1:

        for k, v in curr.characters.items():
            # append current to LCP
            lcp += k

            # update curr pointer to child node
            curr = v
    return lcp
        

# given set of keys
words = [
    "code", "coder", "coding", "codable", "codec", "codecs", "coded",
    "codeless", "codependence", "codependency", "codependent",
    "codependents", "codes", "codesign", "codesigned", "codeveloped",
    "codeveloper", "codex", "codify", "codiscovered", "codrive"
]

print("Longest Common Prefix is:", LCPPrefix(words))
