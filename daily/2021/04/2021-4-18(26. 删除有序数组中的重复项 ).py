class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        cur = 0
        while cur < n:
            tail = cur + 1
            while tail < n and nums[tail] == nums[cur]:
                tail += 1
            nums[res] = nums[cur]
            cur = tail
            res += 1
        return res