from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n = len(nums)
        res = []
        
        for item in count:
            if count[item] > n/3:
                res.append(item)

        return res


        