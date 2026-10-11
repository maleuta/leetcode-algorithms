from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1

        res = 0

        while left < right:
            if heights[left] < heights[right ]:
                amountl = min(heights[left], heights[right]) * (right - left)
                res = max(res, amountl)
                left += 1
            elif heights[left] > heights[right]:
                amountr = min(heights[left], heights[right]) * (right - left)
                res = max(res, amountr)
                right -= 1
            else:
                amount = min(heights[left], heights[right]) * (right - left)
                res = max(res, amount)
                left += 1
                right -= 1
        
        return res


print(Solution().maxArea([1,7,2,5,4,7,3,6]))