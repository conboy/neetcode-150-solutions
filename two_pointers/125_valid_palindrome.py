class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'\W+', '', s).replace('_', '').lower()

        print(s)

        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True