class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        pre_xor = [0]
        for x in arr:
            pre_xor.append(x ^ pre_xor[-1])
        ans = []
        for l, r in queries:
            ans.append(pre_xor[r + 1] ^ pre_xor[l])
        return ans