class Solution:
    def canCross(self, stones: List[int]) -> bool:
        n = len(stones)

        @cache
        def dfs(pos: int, pre_jump: int) -> bool:
            if pos == stones[-1]:
                return True
            for i in range(-1, 2):
                jump = pre_jump + i
                next_pos = pos + jump
                if next_pos <= pos or next_pos > stones[-1]:
                    continue
                idx = bisect.bisect_left(stones, next_pos)
                if idx < n and stones[idx] == next_pos:
                    if dfs(next_pos, jump):
                        return True
            return False

        if stones[1] - stones[0] == 1:
            return dfs(stones[1], 1)
        return False