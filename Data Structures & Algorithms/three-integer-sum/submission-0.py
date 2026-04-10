class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        def twoSum(nums, target):
            res = []
            # make sure nums is sorted
            l, r = 0, len(nums) - 1
            while l < r :
                curr = nums[l] + nums[r]

                if (curr == target):
                    pair = [nums[l], nums[r]]
                    if pair not in res:
                        res.append(pair)
                    l += 1
                    r -= 1
                
                elif (curr > target):
                    r -= 1
                elif (curr < target):
                    l += 1
            return res

        nums.sort()
        res = []
        for i in range(len(nums)):
            curr_nums = nums.copy()
            curr_nums.pop(i)
            twoSumRes = twoSum(curr_nums, -nums[i])
            while twoSumRes:
                print('two sum found')
                currTwoSumRes = twoSumRes.pop()
                currTwoSumRes.append(nums[i])
                currTwoSumRes.sort()
                if currTwoSumRes not in res:
                    res.append(currTwoSumRes)
        return res