from typing import List
import unittest

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price


        
        return max_profit

class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_standard_profit(self):
        """Test a standard array with a clear buy/sell window."""
        self.assertEqual(self.solution.maxProfit([7, 1, 5, 3, 6, 4]), 5)
        self.assertEqual(self.solution.maxProfit([10, 1, 5, 6, 7, 1]), 6)

    def test_no_profit(self):
        """Test arrays where prices only go down (should return 0)."""
        self.assertEqual(self.solution.maxProfit([10, 8, 7, 5, 2]), 0)
        self.assertEqual(self.solution.maxProfit([7, 6, 4, 3, 1]), 0)

    def test_single_element(self):
        """Test the minimum constraint limit of a single day."""
        self.assertEqual(self.solution.maxProfit([5]), 0)

    def test_flat_prices(self):
        """Test an array where the price never changes."""
        self.assertEqual(self.solution.maxProfit([3, 3, 3, 3, 3]), 0)

    def test_profit_at_extremes(self):
        """Test buying on the first day and selling on the very last day."""
        self.assertEqual(self.solution.maxProfit([1, 2, 3, 4, 5, 100]), 99)

if __name__ == '__main__':
    unittest.main()