class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        tPointer = 0
        for charS in s:
            if tPointer == len(t):
                return 0
            if t[tPointer] == charS:
                tPointer += 1
            
        return len(t) - tPointer

        