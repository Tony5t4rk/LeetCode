from sortedcontainers import SortedList

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3:
            return False

        left_min = nums[0]
        right_nums = SortedList(nums[2:])

        for j in range(1, n - 1):
            if left_min < nums[j]:
                idx = right_nums.bisect_right(left_min)
                if idx < len(right_nums) and nums[j] > right_nums[idx]:
                    return True
            left_min = min(left_min, nums[j])
            right_nums.remove(nums[j + 1])

        return False


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)

        stack = [nums[-1]]
        max_k = float('-inf')
        for i in range(n - 2, -1, -1):
            if nums[i] < max_k:
                return True
            while stack and nums[i] > stack[-1]:
                max_k = stack.pop()
            if nums[i] > max_k:
                stack.append(nums[i])
        return False