class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        def stringToDict(s):
            res = {}
            for char in s:
                if char in res:
                    res[char] += 1
                else:
                    res[char] = 1
            return res

        def permutation(s1, s2):
            return stringToDict(s1) == stringToDict(s2)

        for L in range(len(s2)):
            if permutation(s2[L: L + s1_len], s1):
                #print(s1)
                #print(s2[L: L + s1_len])
                return True

        return False

        