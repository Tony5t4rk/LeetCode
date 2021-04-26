class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def check(x):
            day = 0
            w_sum = 0
            for weight in weights:
                w_sum += weight
                if w_sum > x:
                    day += 1
                    w_sum = weight
            if w_sum != 0:
                day += 1
            return day <= D
        l, r = max(weights), sum(weights)
        while l < r:
            m = (l + r) // 2
            if check(m):
                r = m
            else:
                l = m + 1
        return l