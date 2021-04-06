class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        ptr = 0
        cur = 0
        while cur < n:
            tail = cur + 1
            while tail < n and nums[tail] == nums[cur]:
                tail += 1
            if tail - cur > 1:
                nums[ptr] = nums[cur]
                nums[ptr + 1] = nums[cur]
                ptr += 2
            else:
                nums[ptr] = nums[cur]
                ptr += 1
            cur = tail
        return ptr