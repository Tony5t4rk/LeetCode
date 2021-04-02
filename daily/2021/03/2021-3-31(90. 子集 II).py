class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        cnt, book = {}, {}
        for num in nums:
            book[num] = 0
            if num in cnt:
                cnt[num] += 1
            else:
                cnt[num] = 1
        arr = []
        for k, v in cnt.items():
            arr.append(k)
        result = []
        def dfs(idx):
            if idx == len(arr):
                buf = []
                for i in arr:
                    for j in range(book[i]):
                        buf.append(i)
                result.append(buf)
                return
            for i in range(cnt[arr[idx]] + 1):
                book[arr[idx]] = i
                dfs(idx + 1)
        dfs(0)
        return result