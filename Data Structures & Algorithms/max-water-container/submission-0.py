class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_i = 0
        right_i = len(heights) - 1

        max_size = 0

        while left_i != right_i:
            print(right_i)
            water_height = min(heights[left_i], heights[right_i])
            water_length = right_i - left_i
            size = water_height * water_length
            if size > max_size:
                max_size = size

            if heights[left_i] <= heights[right_i]:
                left_i += 1
            else:
                right_i -= 1

        return max_size
        