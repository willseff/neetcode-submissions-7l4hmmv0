class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        queue=[]
        for num in asteroids:
            discard = False
            while queue and queue[-1] > 0 and num < 0:
                if abs(queue[-1]) >  abs(num):
                    discard = True
                    break
                elif abs(queue[-1]) == abs(num):
                    discard = True
                    queue.pop()
                    break
                else:
                    queue.pop()
            
            if not discard:
                queue.append(num)

        return queue
                


