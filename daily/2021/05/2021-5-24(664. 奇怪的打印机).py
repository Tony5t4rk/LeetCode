class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j - 1]
                else:
                    mi = float('inf')
                    for k in range(i, j):
                        mi = min(mi, dp[i][k] + dp[k + 1][j])
                    dp[i][j] = mi
        return dp[0][n - 1]