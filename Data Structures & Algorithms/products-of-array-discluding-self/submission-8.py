class Solution:
    def list_prod(self, nums: List[int]) -> int:
        prod = 1
        for num in nums:
            prod = prod * num

        return prod

    def drop_first_zero(self, nums):
        zero_indices = [i for i in range(len(nums)) if nums[i] == 0]
        nums.pop(zero_indices[0])
        return nums

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        grand_prod = self.list_prod(nums)

        return [int(grand_prod/x) if x != 0 else self.list_prod(self.drop_first_zero(nums.copy())) for x in nums]

        
        