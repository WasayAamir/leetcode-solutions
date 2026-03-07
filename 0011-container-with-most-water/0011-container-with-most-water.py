class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)


        max_area = 0
        l = 0
        r = n - 1

        while l < r:
            area = (r-l) * min(height[l], height[r])
            max_area = max(max_area, area) 

            if height [l] < height[r]:
                l = l + 1
            else:
                r = r - 1

        return max_area