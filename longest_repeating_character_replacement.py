class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_count = 0
        count = [0] * 26

        for right in range(len(s)):
            count[ord(s[right]) - ord('A')] += 1
            max_count = max(max_count, count[ord(s[right]) - ord('A')])

            while right - left + 1 - max_count > k:
                count[ord(s[left]) - ord('A')] -= 1
                left += 1

        return right - left + 1

s = "ABAB"
k = 2

result = Solution().characterReplacement(s, k)
print(result)
