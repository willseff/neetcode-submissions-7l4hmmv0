class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        found = False
        window_nums= {}
        for num in nums[0:k+1]:
            if num in window_nums:
                #window_nums[num] += 1
                return True
            else:
                window_nums[num] = 1
        
        for R in range(k+1, len(nums)):
            window_nums.pop(nums[R-k-1])
            if nums[R] in window_nums:
                return True
            else:
                window_nums[nums[R]] = 1
        
        return False


            


