L = 30

class Node:
    def __init__(self, zero=None, one=None):
        self.zero = zero
        self.one = one

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, x: int):
        cur = self.root
        for i in range(L, -1, -1):
            if (1 << i) & x == 0:
                if not cur.zero:
                    cur.zero = Node()
                cur = cur.zero
            else:
                if not cur.one:
                    cur.one = Node()
                cur = cur.one

    def get_max_xor(self, x: int) -> int:
        ans, cur = 0, self.root
        for i in range(L, -1, -1):
            if (1 << i) & x == 0:
                if cur.one:
                    cur = cur.one
                    ans |= (1 << i)
                else:
                    cur = cur.zero
            else:
                if cur.zero:
                    cur = cur.zero
                    ans |= (1 << i)
                else:
                    cur = cur.one
        return ans

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n, q = len(nums), len(queries)
        nums.sort()
        queries = sorted([(x, m, i) for i, (x, m) in enumerate(queries)], key=lambda query: query[1])

        ans = [0] * q
        trie = Trie()
        idx = 0
        for x, m, qid in queries:
            while idx < n and nums[idx] <= m:
                trie.insert(nums[idx])
                idx += 1
            if idx == 0:
                ans[qid] = -1
            else:
                ans[qid] = trie.get_max_xor(x)
        return ans