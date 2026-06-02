class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        index = len(digits)-1
        digits[index] += 1
        carry = 0

        while index >= 0:
            number = (digits[index] + carry)
            carry = number // 10 if number >= 10 else 0
            digits[index] = number % 10
            index -= 1
        
        if carry: digits.insert(index + 1, carry)
        return digits