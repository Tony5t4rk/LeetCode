class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = {}
        for num in answers:
            if not num in cnt:
                cnt[num] = 0
            cnt[num] += 1
        ret = 0
        for k, v in cnt.items():
            if k == 0:
                ret += v
                continue
            ret += (k + 1) * ((v + k) // (k + 1))
        return ret
