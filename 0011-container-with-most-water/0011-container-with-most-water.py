class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0 
        l = 0
        r = len(height) - 1
        while l < r:
            area = (r - l)* min(height[l], height[r])
            res = max(res,area) # which ever is bigger
            if height[l] < height[r]:
                l += 1
            elif height[r] < height[l]:
                r -= 1
            else:
                l += 1
        return res 


# Time Complexity
# Linear Time : O(n) which is amazing.