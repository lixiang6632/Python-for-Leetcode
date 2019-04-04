class Solution:
    def reverse(self, x: int) -> int:
        result = int(str(abs(x))[::-1])
        if abs(result) > 2147483647:
            return 0
        if x < 0:
            return - result
        return result