class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nxt = [None] * 27

    def searchPrefix(self, prefix: str) -> 'Trie':
        cur = self
        for c in prefix:
            idx = ord(c) - ord('a') + 1
            if not cur.nxt[idx]:
                return None
            cur = cur.nxt[idx]
        return cur

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self
        for c in word:
            idx = ord(c) - ord('a') + 1
            if not cur.nxt[idx]:
                cur.nxt[idx] = Trie()
            cur = cur.nxt[idx]
        cur.nxt[0] = Trie

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tail = self.searchPrefix(word)
        return True if tail and tail.nxt[0] else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tail = self.searchPrefix(prefix)
        return True if tail else False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)