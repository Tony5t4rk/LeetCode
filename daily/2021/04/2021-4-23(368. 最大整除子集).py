class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        dp = [1] * n
        max_size = 1
        max_val = nums[0]
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                if dp[i] >= max_size:
                    max_size = dp[i]
                    max_val = nums[i]

        res = []
        if max_size == 1:
            res.append(max_val)
            return res

        for i in range(n - 1, -1, -1):
            if dp[i] == max_size and max_val % nums[i] == 0:
                res.append(nums[i])
                max_val = nums[i]
                max_size -= 1

        return res