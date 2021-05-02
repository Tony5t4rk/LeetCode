class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        h = len(wall)
        mp = {}
        for i in range(h):
            pre_sum = 0
            for j in range(len(wall[i]) - 1):
                pre_sum += wall[i][j]
                if pre_sum in mp:
                    mp[pre_sum] += 1
                else:
                    mp[pre_sum] = 1
        return h if not mp else h - max(mp.values())