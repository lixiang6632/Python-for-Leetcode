class Solution:
    def romanToInt(self, s: str) -> int:
        doubles = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4 }
        singles = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        result, i = 0, 0
        s_len = len(s)
        while i < s_len:
            if i < s_len - 1 and s[i:i+2] in doubles:
                result += doubles[s[i:i+2]]
                i += 2
            else:
                result += singles[s[i]]
                i += 1
        return result