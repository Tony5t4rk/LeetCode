class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        pre_max = [height[0]] + [0] * (n - 1)
        for i in range(1, n):
            pre_max[i] = max(pre_max[i - 1], height[i])

        suf_max = [0] * (n - 1) + [height[n - 1]]
        for i in range(n - 2, -1, -1):
            suf_max[i] = max(suf_max[i + 1], height[i])

        return sum(min(pre_max[i], suf_max[i]) - height[i] for i in range(n))
