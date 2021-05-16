HIGH_DIGIT = 30

class Node:
    def __init__(self, zero=None, one=None):
        self.zero = zero
        self.one = one

class Trie:
    def __init__(self):
        self.root = Node()
    
    def add(self, x):
        cur = self.root
        for i in range(HIGH_DIGIT, -1, -1):
            if (1 << i) & x:
                if cur.one is None:
                    cur.one = Node()
                cur = cur.one
            else:
                if cur.zero is None:
                    cur.zero = Node()
                cur = cur.zero
    
    def check(self, x):
        cur = self.root
        y = 0
        for i in range(HIGH_DIGIT, -1, -1):
            if (1 << i) & x:
                if cur.zero is not None:
                    cur = cur.zero
                elif cur.one is not None:
                    cur = cur.one
                    y += (1 << i)
                else:
                    break
            else:
                if cur.one is not None:
                    cur = cur.one
                    y += (1 << i)
                elif cur.zero is not None:
                    cur = cur.zero
                else:
                    break
        return x ^ y

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        ans = 0
        for num in nums:
            trie.add(num)
            ans = max(ans, trie.check(num))
        return ans