class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        L, R = 0, len(people)-1
        res = 0
        while L < R:
            print('step' + str(L) + str(R))
            if people[L] + people[R] <= limit:
                L += 1 
                R -= 1
            else:
                R -= 1
            res += 1
        
        if L == R: res += 1
        
        return res
