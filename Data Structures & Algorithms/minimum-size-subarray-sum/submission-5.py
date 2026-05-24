class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        min_length = 999999999
        window_sum = 0
        found = False

        for R in range(len(nums)):
            window_sum += nums[R]
            while window_sum >= target:
                min_length = min(min_length, R-L+1)
                window_sum -= nums[L]
                L += 1
                found = True
        
        return min_length if found else 0


        