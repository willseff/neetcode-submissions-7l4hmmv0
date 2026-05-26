class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        L, R = 0, 0
        min_num_white = 9999999
        num_white = 0
        for R in range(len(blocks)):
            print(R)
            if blocks[R] == 'W':
                num_white += 1

            if (R-L+1)==k:
                print('size reached')
                min_num_white = min(min_num_white, num_white)
                if blocks[L] == 'W':
                    num_white -= 1
                L += 1
                #min_num_white = min(min_num_white, num_white)

        return min_num_white
        

            
        