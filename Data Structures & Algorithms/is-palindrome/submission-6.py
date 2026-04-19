class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        s = re.sub("\W", "", s)
        left, right = 0, len(s) - 1
        print(s)
        while left < right:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True