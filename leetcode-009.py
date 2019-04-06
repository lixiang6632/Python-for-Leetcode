class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        x_reverse = x[::-1]
        if x  == x_reverse:
            return True
        return False