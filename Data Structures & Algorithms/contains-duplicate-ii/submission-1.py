class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        found = False
        window_nums= set()
        for num in nums[0:k+1]:
            if num in window_nums:
                return True
            else:
                window_nums.add(num)
        
        for R in range(k+1, len(nums)):
            window_nums.remove(nums[R-k-1])
            if nums[R] in window_nums:
                return True
            else:
                window_nums.add(nums[R])
        
        return False


            


