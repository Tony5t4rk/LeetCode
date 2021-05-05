class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        max_num = max(nums)
        cnt = [0] * (max_num + 1)
        for num in nums:
            cnt[num] += num
        dp = [cnt[0], max(cnt[0], cnt[1])]
        cur = 0
        for i in range(2, max_num + 1):
            dp[cur] = max(dp[cur] + cnt[i], dp[cur ^ 1])
            cur ^= 1
        return max(dp)