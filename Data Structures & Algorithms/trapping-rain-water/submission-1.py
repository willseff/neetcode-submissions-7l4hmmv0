class Solution:
    def trap(self, height: List[int]) -> int:
        res =  0
        for i in range(1, max(height)+1):
            layer = [x >= i for x in height]
            while not layer[0]:
                layer.pop(0)
            while not layer[-1]:
                layer.pop()
            
            res += sum([not x for x in layer])

        return res


