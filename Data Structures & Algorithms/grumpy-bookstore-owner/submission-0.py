class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        grumpyCust = [x * y for x, y in zip(customers, grumpy)]
        servedCust = [x if y == 0  else 0 for x, y in zip(customers, grumpy)]

        maxWindow = grumpWindow = sum(grumpyCust[0:minutes])

        for i in range(minutes, len(grumpyCust)):
            grumpWindow += grumpyCust[i]
            grumpWindow -= grumpyCust[i-minutes]
            maxWindow = max(maxWindow, grumpWindow)

        return maxWindow + sum(servedCust)

        



        