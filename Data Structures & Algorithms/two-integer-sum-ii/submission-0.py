class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left_i = 0 
        right_i = len(numbers) - 1 

        sol_found = False

        while not sol_found:
            #print("current total: " + curr_total)
            curr_total = numbers[left_i] + numbers[right_i] 
            if curr_total < target:
                left_i += 1
            
            elif curr_total > target:
                right_i -= 1

            else: 
                sol_found = True

        return [left_i + 1, right_i + 1]
        
        