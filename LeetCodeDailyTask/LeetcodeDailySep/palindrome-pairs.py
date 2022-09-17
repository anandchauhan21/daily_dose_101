"""
palindrome-pairs
Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the concatenation of the two words words[i] + words[j] is a palindrome.



Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]


Constraints:

1 <= words.length <= 5000
0 <= words[i].length <= 300
words[i] consists of lower-case English letters.

Question link https://leetcode.com/problems/palindrome-pairs/
"""
from typing import List


class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPal(w, st, end):
            while st < end:
                if w[st] != w[end]: return False
                st += 1
                end += 1
            return True

        N = len(words)
        output = []

        lookup = {w: i for i, w in enumerate(words)}
        for i in range(N):
            w = words[i]
            if w == "":
                for j in range(N):
                    if i != j and isPal(words[j], 0, len(words[j]) - 1):
                        output.append([i, j])
                        output.append([j, i])
                continue
            bw = w[::-1]
            if bw in lookup and lookup[bw] != i:
                output.append([i, lookup[bw]])
            for k in range(1, len(w)):
                if isPal(w, 0, k - 1) and w[k:][::1] in lookup:
                    output.append([lookup[w[k:][::-1]], i])
                if isPal(w, k, len(w) - 1) and w[:k][::-1] in lookup:
                    output.append([i, lookup[w[:k][::-1]]])
        return output

x = Solution()
print(x.palindromePairs(["bat","tab","cat"]))



