class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        if s_len == 1 or s_len == 0:
            return s
        len_result = 0
        for index, ch in enumerate(s):
            start, end = index, index
            while start > 0 and end < s_len - 1 and s[start] == s[end]:
                start -= 1
                end += 1
            if s[start] != s[end]:
                start += 1
                end -= 1
            if end - start + 1 > len_result:
                len_result = end - start + 1
                result_start = start
                result_end = end
        for index, ch in enumerate(s[:-1]):
            start, end = index, index + 1
            while start > 0 and end < s_len - 1 and s[start] == s[end]:
                start -= 1
                end += 1
            if s[start] != s[end]:
                start += 1
                end -= 1
            if end - start + 1 > len_result:
                len_result = end - start + 1
                result_start = start
                result_end = end
        return s[result_start : result_end + 1]