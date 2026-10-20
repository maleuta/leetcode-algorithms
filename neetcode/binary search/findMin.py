from typing import List
import unittest

class Solution:
    def findMin(self, nums: List[int]) -> int:

        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]


        # 2 option  
        # l, r = 0, len(nums) - 1

        # if nums is None:
        #     return 0

        # res = float('inf')

        # while l <= r:
        #     if nums[l] < nums[r]:
        #         res = min(res, nums[l])
        #         break
        #     mid = (l + r) // 2
        #     res = min(res, nums[mid])

        #     if nums[mid] >= nums[l]:
        #         l = mid + 1
        #     else:
        #         r = mid - 1


        # return res
        

class testForFindMin(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_basic_options(self):
        self.assertEqual(self.sol.findMin([3,4,5,6,1,2]), 1)
        self.assertEqual(self.sol.findMin([4,5,0,1,2,3]), 0)

    def test_no_array(self):
        self.assertEqual(self.sol.findMin([1]), 1)

    def test_simple_array(self):
        self.assertEqual(self.sol.findMin([1,2,3,4,5,6]), 1)


if __name__ == '__main__':
    unittest.main()