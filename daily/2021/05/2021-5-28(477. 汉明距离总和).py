class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(30):
            o = sum(((num >> i) & 1) for num in nums)
            ans += o * (n - o)
        return ans