from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []

        for i in range (len(nums) - 2):
            left, right = i+1, len(nums)-1

            if i > 0 and nums[i] == nums[i - 1]:
                continue

            while left < right:
                if nums[left] + nums[right] == -nums[i]:
                    add = [nums[i], nums[left], nums[right]]
                    res.append(add)

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1

                elif nums[left] + nums[right] > -nums[i]:
                    right -= 1

                elif nums[left] + nums[right] < -nums[i]:
                    left += 1



        return res if res is not None else []


print(Solution().threeSum([-1,0,1,2,-1,-4]))