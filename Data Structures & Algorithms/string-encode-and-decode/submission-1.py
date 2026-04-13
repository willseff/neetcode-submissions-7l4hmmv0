class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            part = str(len(string)) + "#" + string
            encoded = encoded + part
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        res = []
        charList = list(s)
        curr = ''
        while charList:
            #print(charList)
            numString = ''
            while charList[0] != '#':
                #print("pop charlist")
                curr = charList.pop(0)
                #print('currValue to append: ' + curr)
                numString = numString + curr
            
            # pop the hashtag
            charList.pop(0)
            wordString = ''
            #print(numString)
            for i in range(int(numString)):
                wordString += charList.pop(0)
            
            res.append(wordString)
        
        return res




            


        
