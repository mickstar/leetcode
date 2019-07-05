class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_score = 0
        for x in range(len(s)):
            current_score = 0
            characters = set()
            for y in range(x, len(s)):
                if s[y] in characters:
                    break
                characters.add(s[y])
                current_score += 1
            max_score = max(current_score, max_score)
        return max_score
