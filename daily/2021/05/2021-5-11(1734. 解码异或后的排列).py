class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1
        
        first = reduce(xor, range(n + 1))
        for i in range(1, n, 2):
            first ^= encoded[i]
        
        perm = [first]
        for x in encoded:
            perm.append(perm[-1] ^ x)
        
        return perm