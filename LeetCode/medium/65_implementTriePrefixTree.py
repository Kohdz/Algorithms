# https://leetcode.com/problems/implement-trie-prefix-tree/


class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        
class Trie:
    '''
    Time addWord: O(L) | search O(L) | L = len(word)
    Space O (N*L)
    '''
    
    def __init__(self):
        self.rootNode = TrieNode()
        
    # Inserts a word into the trie.
    def insert(self, word: str) -> None:
        currNode = self.rootNode
        for ch in word:                     
            if( ch not in currNode.children ):
                currNode.children[ch] = TrieNode()          
            currNode = currNode.children[ch]        # currnode.children[ch]
        currNode.endOfWord = True
    
    # Returns if the word is in the trie.
    def search(self, word: str) -> bool:
        currNode = self.rootNode                    
        for char in word:
            if(char not in currNode.children):
                return False
            currNode = currNode.children[char]
        return currNode.endOfWord
    
    # Returns if there is any word in the trie that starts with the given prefix.
    def startsWith(self, prefix: str) -> bool:
        currNode = self.rootNode                            
        for char in prefix:
            if(char not in currNode.children):
                return False
            currNode = currNode.children[char]
        return True
    
    # Given a string cat, ( cattle is in trie already), this function 
    # returns, how many prefix characters it matches
    def searchSubstring(self, word: str) -> int:
        currNode = self.rootNode
        for i, char in enumerate(word):
            if(char not in currNode.children):
                return False
            currNode = currNode.children[char]
            if( currNode.endOfWord ):
                return i + 1
        return -1

trie = Trie()

print(trie.insert("apple"))
print(trie.search("apple"))
print(trie.search("app"))
print(trie.startsWith("app"))
print(trie.insert("app"))
print(trie.search("app"))


#################################################################################################################
# Array Version
class NodeII:
    def __init__(self):
        self.children = [None]*26
        self.isLeaf = False
    
class TrieII:

    def __init__(self):
        self.root = NodeII()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                cur.children[i] = NodeII()
            cur = cur.children[i]
        cur.isLeaf = True

    def search(self, word: str) -> bool:
        end = self.findPrefixEnd(word)
        return end and end.isLeaf

    def startsWith(self, prefix: str) -> bool:
        return bool(self.findPrefixEnd(prefix))  
        
    def findPrefixEnd(self, prefix: str) -> NodeII:
        cur = self.root
        for c in prefix:
            i = ord(c) - ord('a')
            if not cur.children[i]:
                return None
            cur = cur.children[i]
        return cur