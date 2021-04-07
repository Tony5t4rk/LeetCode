class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return True if target in nums else False


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        if n == 1:
            return True if nums[0] == target else False
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True
            if nums[l] == nums[m] and nums[m] == nums[r]:
                l += 1
                r -= 1
            elif nums[l] <= nums[m]:
                if nums[l] <= target and target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] < target and target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False