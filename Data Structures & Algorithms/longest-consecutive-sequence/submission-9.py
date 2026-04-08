class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        print(nums)
        current_seq_len = 1
        longest_seq_len = 1
        try:
            previous_num = nums.pop(0)
        except:
            return 0

        for num in nums:
            print("---------")
            print("Current Num: " + str(num))
            print("Previous Num: " + str(previous_num))
            print("Current Seq Len: " + str(current_seq_len))
            if num == (previous_num + 1):
                current_seq_len += 1

            else:
                if current_seq_len > longest_seq_len:
                    longest_seq_len = current_seq_len
                    
                else: 
                    pass
                current_seq_len = 1

            previous_num = num

        return max(longest_seq_len, current_seq_len)


        