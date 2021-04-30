class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = {}
        for num in nums:
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1
            if cnt[num] == 3:
                del cnt[num]
        return cnt.popitem()[0]