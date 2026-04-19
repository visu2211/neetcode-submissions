class Solution:
    def isPalindrome(self, s: str) -> bool:
        up = ""
        for c in s:
            if c.isalnum():
                up += c.lower()
        print(up)
        return up == up[::-1]