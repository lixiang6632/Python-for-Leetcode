class Solution:
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        result = 0
        while start < end:
            result = max(result, (end - start) * min(height[start], height[end]))
            if height[start] < height[end]:
                temp = height[start]
                start += 1
                while start < end and height[start] < temp:
                    start += 1
            else:
                temp = height[end]
                end -= 1
                while start < end and height[end] < temp:
                    end -= 1
        return result