#Leftmost Non-repeating Element
class Solution:
    def firstUniqChar(s: str) -> int:
        count = [0] * 26
        for i in s:
            count[ord(i) - 97] += 1
        for i in range(len(s)):
            if count[ord(s[i]) - 97] == 1:
                return i
                break
        return -1
t = Solution
print(t.firstUniqChar("leetcode"))
