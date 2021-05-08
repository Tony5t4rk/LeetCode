class Solution:
    work = []

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        jobs.sort(reverse=True)

        def dfs(idx: int, limit: int):
            if idx == n:
                return True
            for i in range(k):
                if self.work[i] + jobs[idx] <= limit:
                    self.work[i] += jobs[idx]
                    if dfs(idx + 1, limit):
                        return True
                    self.work[i] -= jobs[idx]
                if self.work[i] == 0:
                    break
            return False

        l, r = max(jobs), sum(jobs)
        while l < r:
            m = (l + r) // 2
            self.work = [0] * k
            if dfs(0, m):
                r = m
            else:
                l = m + 1
        return l