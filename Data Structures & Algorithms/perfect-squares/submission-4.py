import sys
sys.setrecursionlimit(10000)
class Solution:
    def numSquares(self, n: int) -> int:
        cache = {}
        def mem(n):
            if n in cache:
                return cache[n]

            possibleSquares = []
            for i in range(n):
                if (i+1)**2 > n: 
                    break
                possibleSquares.append((i+1)**2)
            
            if n in possibleSquares:
                return 1

            subtract = [mem(n - x) for x in possibleSquares]

            cache[n] = min(subtract) + 1

            return cache[n]

        return mem(n)
        