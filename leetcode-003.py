class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashmap, start, length = {}, 0, 0
        for index, ch in enumerate(s):
            if ch in hashmap:
                length = max(length, index-start)
                start = max(start, hashmap[ch]+1)               
            hashmap[ch] = index
        return max(length, len(s)-start)