class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        mp = {0: -1}
        pre_sum = 0
        ans = 0
        for idx, num in enumerate(nums):
            if num == 0:
                pre_sum -= 1
            elif num == 1:
                pre_sum += 1
            if pre_sum in mp:
                ans = max(ans, idx - mp[pre_sum])
            else:
                mp[pre_sum] = idx
        return ans