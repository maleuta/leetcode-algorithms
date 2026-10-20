from typing import List
import unittest

"""
speed complexity is O(nlogm), where n = len(piles) and m is the max number of bananas in a pile, 
cause I'n using binary search, space complexity is O(1)
"""
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right
        

        while left <= right:
            k = (left + right) // 2

            total_h = 0
            for p in piles:
                total_h += (p + k - 1 ) // k

            if total_h <= h:
                res = k
                right = k - 1
            else:
                left = k + 1

        return res



class Testing(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_standard(self):
        self.assertEqual(self.sol.minEatingSpeed([1, 4, 3, 2], 9), 2)
        self.assertEqual(self.sol.minEatingSpeed([1, 4, 3, 2], 9), 2)

    def test_hours_equals_piles_length(self):
        self.assertEqual(self.sol.minEatingSpeed([30, 11, 23, 4, 20], 5), 30)

    def test_plenty_of_hours(self):
        self.assertEqual(self.sol.minEatingSpeed([1, 34, 5, 6, 7, 10], 100), 1)

    def test_single_pile(self):
        self.assertEqual(self.sol.minEatingSpeed([10], 3), 4)


if __name__ == '__main__':
    unittest.main()
            



        