from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        n, m = len(matrix), len(matrix[0])
        ans = float('-inf')
        for top in range(n):
            col_sum = [0] * m
            for bot in range(top, n):
                for i in range(m):
                    col_sum[i] += matrix[bot][i]
                st = SortedList([0])
                pre_sum = 0
                for x in col_sum:
                    pre_sum += x
                    idx = st.bisect_left(pre_sum - k)
                    if idx != len(st):
                        ans = max(ans, pre_sum - st[idx])
                    st.add(pre_sum)
        return ans