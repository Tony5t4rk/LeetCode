class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        cmp_key = lambda x, y: int(str(y) + str(x)) - int(str(x) + str(y))
        nums.sort(key=cmp_to_key(cmp_key))
        res = ''.join(map(str, nums))
        return '0' if res[0] == '0' else res