class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        elif n <= 2:
            return max(nums)
        dp1 = [None] * (n + 1)
        dp1[1], dp1[2] = nums[1], max(nums[1:3])
        for i in range(3, n):
            dp1[i] = max(dp1[i - 1], dp1[i - 2] + nums[i])
        dp2 = [None] * (n + 1)
        dp2[0], dp2[1] = nums[0], max(nums[:2])
        for i in range(2, n - 1):
            dp2[i] = max(dp2[i - 1], dp2[i - 2] + nums[i])
        return max(dp1[n - 1], dp2[n - 2])