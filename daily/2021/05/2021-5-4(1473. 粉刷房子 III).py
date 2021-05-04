class Solution:
    def minCost(self, houses: List[int], cost: List[List[int]], m: int, n: int, target: int) -> int:
        houses = list(map(lambda x: x - 1, houses))
        dp = [[[float('inf')] * target for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if houses[i] != -1 and j != houses[i]:
                    continue
                for k in range(target):
                    for l in range(n):
                        if l == j:
                            if i == 0:
                                if k == 0:
                                    dp[i][j][k] = 0
                            else:
                                dp[i][j][k] = min(dp[i][j][k], dp[i - 1][j][k])
                        elif i > 0 and k > 0:
                            dp[i][j][k] = min(dp[i][j][k], dp[i - 1][l][k - 1])
                    if dp[i][j][k] != float('inf') and houses[i] == -1:
                        dp[i][j][k] += cost[i][j]
        ans = min(dp[m - 1][j][target - 1] for j in range(n))
        return -1 if ans == float('inf') else ans