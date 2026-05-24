class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        found = False
        window_nums= set()
        for R in range(len(nums)):
            if nums[R] in window_nums:
                return True
            window_nums.add(nums[R])
            if R >= k:
                window_nums.remove(nums[R-k])
        
        return False 


            


