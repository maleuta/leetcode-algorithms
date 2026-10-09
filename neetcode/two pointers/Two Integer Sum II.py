from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using two pointers

        left, right = 0, len(numbers) - 1
        res = []

        while (left < right):
            if (numbers[left] + numbers[right]) > target:
                right -= 1
            
            if numbers[left] + numbers[right] < target:
                left += 1

            if numbers[left] + numbers[right] == target:
                res.append(left + 1)
                res.append(right + 1)
                break

        return res

        
print(Solution().twoSum([1,2,3,4], 3))