class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)

        pre_xor = [0]
        for x in arr:
            pre_xor.append(x ^ pre_xor[-1])

        cnt = 0
        for i in range(1, n + 1):
            for k in range(i + 1, n + 1):
                if pre_xor[k] == pre_xor[i - 1]:
                    cnt += k - i
        return cnt