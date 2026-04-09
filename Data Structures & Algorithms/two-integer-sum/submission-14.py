class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        d = {}
        for num in nums:
            d[num] = i 
            i += 1
        
        i = 0
        for num in nums:
            complement = target-num
            if (complement in d) and (d[complement] != i):
                return [i, d[complement]]
            i += 1






