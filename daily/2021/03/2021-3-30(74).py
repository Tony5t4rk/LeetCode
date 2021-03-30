class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arr = []
        for row in matrix:
            arr += row
        l, r = 0, len(arr)
        if l == r:
            if arr[l] == target:
                return True
            else:
                return False
        while l < r:
            m = (l + r) // 2
            if arr[m] <= target:
                l = m + 1
            else:
                r = m
        if l == 0:
            return False
        elif target == arr[l - 1]:
            return True
        return False
