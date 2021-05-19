class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        pre_xor = [[0] * (n + 1) for _ in range(m + 1)]
        arr = []
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                pre_xor[i][j] = pre_xor[i - 1][j] ^ pre_xor[i][j - 1] ^ pre_xor[i - 1][j - 1] ^ matrix[i - 1][j - 1]
                arr.append(pre_xor[i][j])
        arr.sort(reverse=True)
        return arr[k - 1]