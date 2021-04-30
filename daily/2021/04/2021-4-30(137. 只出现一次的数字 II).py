class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = collections.Counter(nums)
        ans = [num for num, occ in cnt.items() if occ == 1][0]
        return ans