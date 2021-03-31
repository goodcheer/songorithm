# brute-force took 864ms 
# TrieNode took 208ms

class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}
    
    def __getitem__(self, key):
        return self.children[key]
    
    def __setitem__(self, key, value):
        self.children[key] = value
    
    def __contains__(self, key):
        return key in self.children

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        # e.g. word = apple
        node = self.root 
        for char in word: # a p p l e
            if char not in node:
                node[char] = TrieNode() # {a: TrieNode()}
            node = node[char] # node = TrieNode "a" -> TrieNode "p" -> TrieNode "p" -> TrieNode "l" -> TrieNode "e"
        node.word = True # only last char "e" makes up the word with path "a -> p -> p-> l -> e == apple"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return node.word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
        