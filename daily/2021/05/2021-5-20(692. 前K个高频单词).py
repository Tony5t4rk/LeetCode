class Word:
    def __init__(self, word, num):
        self.word = word
        self.num = num
    
    def __lt__(self, other):
        if self.num != other.num:
            return self.num < other.num
        return self.word > other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = collections.Counter(words)
        heap = []
        for word, num in cnt.items():
            heapq.heappush(heap, Word(word, num))
            if len(heap) > k:
                heapq.heappop(heap)
        heap.sort(reverse=True)
        return [x.word for x in heap]