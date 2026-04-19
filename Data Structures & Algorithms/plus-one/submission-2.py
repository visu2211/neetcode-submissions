class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        carry = 0
        if digits[-1] >= 10:
            carry = 1
            digits[-1] -= 10
        
        i = len(digits) - 2
        while carry:
            if i < 0:
                break
            digits[i] += 1
            carry = 0
            if digits[i] >= 10:
                carry = 1
                digits[i] -= 10
            i -= 1
        if carry:
            digits.insert(0, 1)

        return digits