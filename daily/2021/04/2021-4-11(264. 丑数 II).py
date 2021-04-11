class Solution:
    def nthUglyNumber(self, n: int) -> int:
        xs = [2, 3, 5]
        used, heap = {1}, [1]
        for i in range(n - 1):
            cur = heapq.heappop(heap)
            for x in xs:
                nxt = cur * x
                if not nxt in used:
                    used.add(nxt)
                    heapq.heappush(heap, nxt)
        return heapq.heappop(heap)