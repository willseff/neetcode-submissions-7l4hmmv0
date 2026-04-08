class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_count_dict = {}
        for num in set(nums):
            num_count = len([i for i in nums if i == num])
            if num_count in num_count_dict:
                num_count_dict[num_count].append(num)
            else:
                num_count_dict[num_count] = [num]
        print(num_count_dict)

        top_k = []
        current_freq = len(nums)
        while len(top_k) < k:
            if current_freq in num_count_dict:
                top_k.extend(num_count_dict[current_freq])
            current_freq -= 1

        return top_k



            



        