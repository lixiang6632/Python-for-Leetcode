class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        result = 0
        for index in range(len(s) - 1):
            if roman_map[s[index]] < roman_map[s[index + 1]]:
                result -= roman_map[s[index]]
            else:
                result += roman_map[s[index]]
        return result + roman_map[s[-1]]