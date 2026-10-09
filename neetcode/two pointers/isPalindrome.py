class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = [c.lower() for c in s if c.isalnum()]

        left, right = 0, len(chars)-1

        while left < right:
            if chars[left] == chars[right]:
                left += 1
                right -= 1
            else:
                return False
            
        return True

print(Solution().isPalindrome("Was it a car or a cat I saw?"))