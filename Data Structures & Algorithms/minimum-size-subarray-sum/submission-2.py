class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L, R = 0, 1
        min_length = 99999999
        current_sum = sum(nums[L:R])
        found = False
        while R < (len(nums) + 1):
            #print("L: " + str(L))
            #print("R: " + str(R))
            #print(current_sum)
            if current_sum >= target:
                min_length = min(min_length, R-L)
                found = True
                current_sum -= nums[L]
                L += 1
            elif current_sum > target and L < R:
                current_sum -= nums[L]
                L += 1
            elif current_sum < target:
                if R < len(nums):
                    current_sum += nums[R]
                R += 1
        
        return 0 if not found else min_length


        