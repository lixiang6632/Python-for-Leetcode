class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p and not s:
            return True
        if (len(p) > 1 and p[1] == '*'):
            return self.isMatch(s, p[2:]) or ((not not s) and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p))
        else:
            return (not not s) and (not not p) and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:]) 