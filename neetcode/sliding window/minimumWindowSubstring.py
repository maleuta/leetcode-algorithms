
"""
Time coomplexity is O(n+m) cause n - length of s, m - length of t;
Space Complexity is O(26) = O(1) cause we have only uppercase letters 
"""

from collections import defaultdict
import unittest

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        lent, lens = len(t), len(s)
        hash_map = defaultdict(int)

        have = 0

        for char in t:
            hash_map[char] += 1

        need = len(hash_map)
        l = 0
        res = [-1, -1]
        res_len = float("inf")

        for i in range(lens):
            char = s[i]
            
            if char in hash_map:
                hash_map[char] -= 1
                if hash_map[char] == 0:
                    have += 1

            while have == need:
                if (i - l + 1) < res_len:
                    res_len = i - l + 1
                    res = [l, i]

                left_char = s[l]
                if left_char in hash_map:
                    hash_map[left_char] += 1
                    if hash_map[left_char] > 0:
                        have -= 1
                
                l += 1

        l, r = res
        return s[l:r + 1] if res_len != float("inf") else ""




        
class TestMinWindow(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_leetcode_examples(self):
        """Test the standard examples provided in the problem description."""
        self.assertEqual(self.sol.minWindow("OUZODYXAZV", "XYZ"), "YXAZ")
        self.assertEqual(self.sol.minWindow("xyz", "xyz"), "xyz")
        self.assertEqual(self.sol.minWindow("x", "xy"), "")

    def test_with_duplicates(self):
        """Test classic substring cases with character duplicates."""
        self.assertEqual(self.sol.minWindow("ADOBECODEBANC", "ABC"), "BANC")

    def test_t_longer_than_s(self):
        """Test when t is longer than s (should return empty string)."""
        self.assertEqual(self.sol.minWindow("a", "aa"), "")

    def test_single_character_match(self):
        """Test matching a single character."""
        self.assertEqual(self.sol.minWindow("a", "a"), "a")

    def test_no_match_exists(self):
        """Test when no valid window can be formed."""
        self.assertEqual(self.sol.minWindow("abcdef", "z"), "")

if __name__ == '__main__':
    unittest.main()