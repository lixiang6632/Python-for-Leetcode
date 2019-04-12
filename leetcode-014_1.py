class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs or '' in strs:
            return ''
        maxlen = min(len(s) for s in strs)
        check, i = 1, 0
        while check != 0 and i < maxlen:
            temp = [s[i] for s in strs]
            if len(set(temp)) == 1:
                i += 1
            else:
                check = 0
        return strs[0][:i]   