class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        for color in set(nums):
            temp = [num for num in nums if num == color]
            res.extend(temp)
        
        for i, j in zip(range(len(nums)), res):
            nums[i] = j
        