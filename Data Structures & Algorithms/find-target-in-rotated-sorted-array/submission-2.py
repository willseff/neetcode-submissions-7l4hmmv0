class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            midVal = nums[mid]
            rVal = nums[r]
            lVal = nums[l]
            if rVal == target:
                return r
            if lVal == target:
                return l

            if (rVal > midVal) and (rVal > target > midVal):
                l = mid + 1
            elif (rVal > midVal):
                r = mid -1
            elif (r < midVal) and (l < target < midVal):
                r = mid -1
            else:
                l = mid + 1
        return -1