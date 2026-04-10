class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        def isValid(d: dict, k):
            counts = []
            for key in d:
                counts.append(d[key])
            
            counts.sort()
            if len(counts) == 1:
                return True
            if sum(counts[:-1]) > k:
                return False
            
            return True
            
        L = 0
        freq_dict = {}
        max_length = 0
        for R in range(len(s)):
            right = s[R]

            if right in freq_dict:
                freq_dict[right] += 1
            else:
                freq_dict[right] = 1

            while not isValid(freq_dict, k):
                left = s[L]
                if freq_dict[left] == 1 :
                    freq_dict.pop(left)
                else:
                    freq_dict[left] -= 1
                
                L += 1
            max_length = max(max_length, R - L + 1)

        
        return max_length

            

            





        