class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums)-1
        if (nums[l] < nums[l+1]) and (nums[l] < nums[r]):
            return nums[l]
        
        while l <= r:
            mid = (l + r) // 2
            rValue = nums[r]
            lValue = nums[l]
            midValue = nums[mid]
            if (mid == 0) and (midValue < nums[mid+1]):
                return midValue
            if (mid == (len(nums)-1)) and (midValue < nums[mid-1]):
                return midValue
            if (midValue < nums[mid+1]) and (midValue < nums[mid-1]):
                return midValue

            if midValue < rValue:
                r = mid-1
            else:
                l = mid+1

