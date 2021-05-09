class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if k * m > len(bloomDay):
            return -1

        def check(x: int) -> bool:
            cur, cnt = 0, 0
            for day in bloomDay:
                if day <= x:
                    cur += 1
                else:
                    cur = 0
                if cur == k:
                    cnt += 1
                    if cnt >= m:
                        break
                    cur = 0
            return cnt >= m

        _l, _r = max(sorted(bloomDay)[:min(len(bloomDay), m * k)]), max(bloomDay)
        while _l < _r:
            _m = (_l + _r) // 2
            if check(_m):
                _r = _m
            else:
                _l = _m + 1
        return _l