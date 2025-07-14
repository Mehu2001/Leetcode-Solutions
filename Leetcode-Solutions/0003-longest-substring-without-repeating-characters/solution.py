class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_str = set()
        c = 0
        max_len = 0
        for i in range(len(s)):
            while s[i] in sub_str:
                sub_str.remove(s[c])
                c += 1
            sub_str.add(s[i])
            max_len = max(max_len, i - c +1)
        return max_len

