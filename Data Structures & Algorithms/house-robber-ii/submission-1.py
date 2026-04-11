class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1 : return nums[0]
        def robSubset(nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            
            if len(nums) == 2:
                return max(nums[1], nums[0])
            
            # each step compute the max if house is robbed vs not robbed
            # if house is robbed then we add that to the max of the house before if it wasn't robbed
            # if house is not robbed then we add 0 to th emax of the house before if it was or was not robbed
            i = 2
            # cannot be robbed, could be robbed
            dp = [nums[0], max(nums[1], nums[0])]
            while i < len(nums):
                print(i)
                print(dp)
                not_robbed = dp[1]
                can_rob = max(nums[i] + dp[0], dp[1])

                dp = [not_robbed, can_rob]

                i += 1
            
            return max(dp)
        nums_pop_first = nums.copy()
        nums_pop_first.pop(0)
        a = robSubset(nums_pop_first)

        nums_pop_last = nums.copy()
        nums_pop_last.pop()
        b = robSubset(nums_pop_last)

        return max(a, b)
            