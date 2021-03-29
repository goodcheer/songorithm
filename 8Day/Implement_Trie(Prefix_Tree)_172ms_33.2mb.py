from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.word = False
        self.children= defaultdict(TrieNode)
        
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
        node = self.root
        for char in word:
            node = node.children[char]
        node.word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.word
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
            

if __name__ == '__main__':
    # Your Trie object will be instantiated and called as such:
    obj = Trie()
    word = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    prefix = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    for idx, w in enumerate(word[1:], 1):
        if w == 'insert':
            obj.insert(prefix[idx][0])
        elif w == 'search':
            print(obj.search(prefix[idx][0]))
        else:
            print(obj.startsWith(prefix[idx][0]))