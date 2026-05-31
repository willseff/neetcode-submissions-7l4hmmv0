class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        nums.insert(0,0)
        zeroIdx = [i for i in range(len(nums)) if nums[i] == 0]
        print(zeroIdx)
        if len(zeroIdx) <= 3:
            return len(nums)-2

        maxLen = 0
        for i in range(2, len(zeroIdx)):
            maxLen = max(zeroIdx[i] - zeroIdx[i-2], maxLen)

        return maxLen-1
        

        