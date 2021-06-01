class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        pre_sum = list(accumulate(candiesCount))
        ans = []
        for favoriteType, favoriteDay, dailyCap in queries:
            l1, r1 = favoriteDay + 1, (favoriteDay + 1) * dailyCap
            l2, r2 = 1 if favoriteType == 0 else pre_sum[favoriteType - 1] + 1, pre_sum[favoriteType]
            ans.append(not(r2 < l1 or l2 > r1))
        return ans