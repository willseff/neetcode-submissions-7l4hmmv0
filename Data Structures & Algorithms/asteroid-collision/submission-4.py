from collections import deque
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        queue = [asteroids.pop(0)]
        for num in asteroids:
            discard = False
            if not queue:
                queue.append(num)
                continue
            # while the last element in the queue and the next num are postive and negative respectively
            while queue and queue[-1] > 0 and num < 0:
                # if the item in the queue is greater than the current then discard current
                if abs(queue[-1]) >  abs(num):
                    discard = True
                    break
        
                # if the item in teh queue is equal to the current discard both
                elif abs(queue[-1]) == abs(num):
                    discard = True
                    queue.pop()
                    break

                # if the item in the queue is less than then remove the queue item then repeat while loop
                else:
                    queue.pop()
            
            if not discard:
                queue.append(num)
            
            #print(queue)

        return queue
                


