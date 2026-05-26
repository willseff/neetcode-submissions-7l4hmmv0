class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minDiff = 99999
        for i in range(k, len(nums)+1):
            window = nums[i-k: i]
            print(window)
            minVal = min(window)
            maxVal = max(window)
            print(maxVal-minVal)
            minDiff = min(minDiff, maxVal-minVal)

        return minDiff

            

