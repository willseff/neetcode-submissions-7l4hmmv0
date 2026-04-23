class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # initialize first window
        firstWindow = s2[0:len(s1)]
        window = {}

        for char in firstWindow:
            if char in window:
                window[char] += 1
            else:
                window[char] = 1

        s1Window = {}
        for char in s1:
            if char in s1Window:
                s1Window[char] += 1
            else:
                s1Window[char] = 1
        if window == s1Window:
                return True

        for i in range(len(s2) - len(s1)):
            #print(i)
            #print(window)
            
            oldChar = s2[i]
            if window[oldChar] == 1:
                window.pop(oldChar)
            else:
                window[oldChar] -= 1

            newChar = s2[i + len(s1)]
            if newChar in window:
                window[newChar] += 1
            else:
                window[newChar] =1

            if window == s1Window:
                return True

        return False



        