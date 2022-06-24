"""
minimum-window-substring
Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in t (including duplicates) is included in the window.
If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.


Constraints:
m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Question link https://leetcode.com/problems/minimum-window-substring/
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        countT, window = {},{}
        for c in t:
            countT[c] = 1+ countT.get(c,0)
        have, need = 0, len(countT)
        res, resLen = [-1,-1],float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1+window.get(c,0)

            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r -l +1)< resLen:
                    res = [l,r]
                    resLen = (r-l +1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1] if resLen != float("infinity") else ""

x = Solution()
print(x.minWindow("ADOBECODEBANC","ABC"))

### out-put: BANC

