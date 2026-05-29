class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        average = sum(arr[0:k])/k
        if average >= threshold:
            numSub = 1
        else:
            numSub = 0
        
        for i in range(k, len(arr)):
            diff = arr[i] - arr[i-k]
            average += diff/k
            if average >= threshold:
                numSub += 1
            
        return numSub
        