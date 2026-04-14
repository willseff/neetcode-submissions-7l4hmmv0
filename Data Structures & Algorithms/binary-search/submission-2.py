class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L, R = 0, len(nums)-1

        while True:
            mid = (L + R) // 2
            if L > R:
                return -1
            print("left: " + str(L) + "right: " + str(R)+ 'mid: ' + str(mid))
            if nums[mid] == target: 
                return mid

            elif nums[mid] < target: 
                L = mid + 1

            else: 
                R = mid - 1
