class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def isvalid(window_hash, target_hash):
            for key in target_hash:
                if key not in window_hash:
                    return False
                
                if window_hash[key] < target_hash[key]:
                    return False
            return True
        L = 0
        window_hash = {}
        target_hash = {}
        min_length = 99999999
        found = False
        min_string = ''

        for char in t:
            if char in target_hash:
                target_hash[char] += 1
            else: 
                target_hash[char] = 1
        
        print("target_hash: " + str(target_hash))

        for R in range(len(s)):
            print("R set to: " + str(R))
            right = s[R]

            if right in window_hash:
                window_hash[right] += 1
            else:
                window_hash[right] = 1
            
            print(window_hash)
        
            # while target hash is a subset of window hash
            while (isvalid(window_hash, target_hash)):
                found = True
                print("L set to: " + str(L))
                # remove the left value and increment L by 1
                left = s[L]

                if window_hash[left] == 1:
                    window_hash.pop(left)
                else:
                    window_hash[left] -= 1

                if (R - L + 1) < min_length:
                    min_string = s[L:R+1]
                min_length = min(min_length, R - L + 1)
                L += 1

        return min_string if found else ""




            

            