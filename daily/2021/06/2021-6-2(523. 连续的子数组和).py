class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        pre_sum = 0
        mp = {0: -1}
        for idx, num in enumerate(nums):
            pre_sum += num
            rem = pre_sum % k
            i = mp.get(rem, idx)
            if i == idx:
                mp[rem] = idx
            elif i <= idx - 2:
                return True
        return False