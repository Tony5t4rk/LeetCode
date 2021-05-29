class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        n, m = len(matrix), len(matrix[0])
        ans = 0
        for top in range(n):
            col_sum = [0] * m
            for bot in range(top, n):
                for i in range(m):
                    col_sum[i] += matrix[bot][i]
                mp = Counter([0])
                pre = 0
                for x in col_sum:
                    pre += x
                    if pre - target in mp:
                        ans += mp[pre - target]
                    mp[pre] += 1
        return ans