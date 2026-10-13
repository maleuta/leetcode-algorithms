class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res_set = set()
        res_num = 0
        res_max = 0

        s.split(',')

        if s is None:
            return 0

        l, r = 0, 0

        for r in range(len(s)):
            while s[r] in res_set:
                res_set.remove(s[l])
                l += 1
            res_set.add(s[r])
            res_num = r - l + 1
            res_max = max(res_num, res_max)


                

        return res_max


def run_tests():
    sol = Solution()
    cases = [
        ("", 0),
        ("a", 1),
        (" ", 1),
        ("aa", 1),
        ("ab", 2),
        ("aaaaa", 1),
        ("abcdef", 6),
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("dvdf", 3),
        ("abcdd", 4),
        ("a1a1", 2),
        ("a" * 10000, 1),
    ]
    for s, expected in cases:
        got = sol.lengthOfLongestSubstring(s)
        status = "OK " if got == expected else "FAIL"
        print(f"{status} s={s[:20]!r:25} expected={expected} got={got}")

run_tests()