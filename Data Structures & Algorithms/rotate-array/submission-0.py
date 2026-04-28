class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotateOnce(nums):
            last = nums.pop()
            nums.reverse()
            nums.append(last)
            nums.reverse()

        for i in range(k):
            rotateOnce(nums)
        