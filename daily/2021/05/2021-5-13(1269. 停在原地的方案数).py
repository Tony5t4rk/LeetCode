class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        
        @cache
        def dfs(step: int, pos: int) -> int:
            ans = 0
            if step == 0:
                return 1 if pos == 0 else 0
            if pos - 1 >= 0:
                ans += dfs(step - 1, pos - 1)
            if pos + 1 < arrLen:
                ans += dfs(step - 1, pos + 1)
            ans += dfs(step - 1, pos)
            return ans
        
        return dfs(steps, 0) % int(1e9 + 7)


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        dp = [[0] * arrLen for _ in range(2)]
        cur = 0
        dp[cur][0] = 1

        for step in range(steps):
            cur ^= 1
            for pos in range(min(arrLen, steps)):
                dp[cur][pos] = dp[cur ^ 1][pos]
                if pos >= 1:
                    dp[cur][pos] += dp[cur ^ 1][pos - 1]
                if pos < arrLen - 1:
                    dp[cur][pos] += dp[cur ^ 1][pos + 1]
        
        return dp[cur][0] % int(1e9 + 7)