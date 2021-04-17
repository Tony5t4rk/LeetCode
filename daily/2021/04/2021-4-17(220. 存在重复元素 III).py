class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        n = len(nums)
        arr = []
        for i in range(n):
            x = nums[i]
            idx = bisect.bisect_left(arr, x)
            if 0 <= idx - 1 < len(arr) and abs(arr[idx - 1] - x) <= t:
                return True
            elif 0 <= idx < len(arr) and abs(arr[idx] - x) <= t:
                return True
            elif 0 <= idx + 1 < len(arr) and abs(arr[idx + 1] - x) <= t:
                return True
            arr.insert(idx, x)
            if i >= k:
                arr.pop(bisect.bisect_left(arr, nums[i - k]))
        return False