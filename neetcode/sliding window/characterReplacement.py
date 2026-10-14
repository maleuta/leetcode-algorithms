from collections import defaultdict
import unittest

# time complexity is O(n), while space complexity is O(m), where m is num of unique characters in a string (aka O(26) = O(1))

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash_map = defaultdict(int)

        l = 0
        max_len = 0
        max_freq_count = 0

        for r in range(len(s)):
            hash_map[s[r]] += 1
            wind_len = r - l + 1

            max_freq_count = max(hash_map.values())

            while (wind_len - max_freq_count) > k:
                hash_map[s[l]] -= 1
                wind_len -= 1
                l += 1


            max_len = max(wind_len, max_len)

        return max_len


class TestCharacterReplacement(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_standard_cases(self):
        self.assertEqual(self.sol.characterReplacement('XYYX', 2), 4)
        self.assertEqual(self.sol.characterReplacement('AAABABBB', 2), 6)
        
    def test_empty_string(self):
        self.assertEqual(self.sol.characterReplacement('', 1), 0)

    def test_zero_k(self):
        self.assertEqual(self.sol.characterReplacement('AABA', 0), 2)
        
    def test_large_k(self):
        self.assertEqual(self.sol.characterReplacement('ABCDE', 5), 5)

if __name__ == '__main__':
    unittest.main()

# def run_tests():
#     sol = Solution()
#     cases= [
#         ('XYYX', 2, 4),
#         ('', 1, 0),
#         ('AABABB', 2, 5),
#     ]
#     for s, k, expected in cases:
#             got = sol.characterReplacement(s, k)
#             status = "OK " if got == expected else "FAIL"
#             print(f"{status} s={s[:20]!r:25} expected={expected} got={got}")

# run_tests()