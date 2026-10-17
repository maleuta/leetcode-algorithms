import unittest


from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid -1

        return -1 


class TestSearch(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    # --- basic / happy path ---
    def test_found_middle(self):
        self.assertEqual(self.sol.search([-1, 0, 3, 5, 9, 12], 9), 4)

    def test_found_left(self):
        self.assertEqual(self.sol.search([-1, 0, 3, 5, 9, 12], -1), 0)

    def test_found_right(self):
        self.assertEqual(self.sol.search([-1, 0, 3, 5, 9, 12], 12), 5)

    # --- not found ---
    def test_not_found(self):
        self.assertEqual(self.sol.search([-1, 0, 3, 5, 9, 12], 2), -1)

    def test_target_smaller_than_all(self):
        self.assertEqual(self.sol.search([1, 3, 5], 0), -1)

    def test_target_larger_than_all(self):
        self.assertEqual(self.sol.search([1, 3, 5], 10), -1)

    # --- edge cases ---
    def test_empty(self):
        self.assertEqual(self.sol.search([], 5), -1)

    def test_single_found(self):
        self.assertEqual(self.sol.search([5], 5), 0)

    def test_single_not_found(self):
        self.assertEqual(self.sol.search([5], 3), -1)

    def test_two_elements(self):
        self.assertEqual(self.sol.search([1, 3], 3), 1)

    def test_duplicates_target_present(self):
        self.assertIn(self.sol.search([1, 2, 2, 2, 3], 2), [1, 2, 3])

    def test_large(self):
        nums = list(range(10000))
        self.assertEqual(self.sol.search(nums, 9999), 9999)
        self.assertEqual(self.sol.search(nums, -1), -1)


if __name__ == "__main__":
    unittest.main()