"""
bag-of-tokens
You have an initial power of power, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.



Example 1:

Input: tokens = [100], power = 50
Output: 0
Explanation: Playing the only token in the bag is impossible because you either have too little power or too little score.
Example 2:

Input: tokens = [100,200], power = 150
Output: 1
Explanation: Play the 0th token (100) face up, your power becomes 50 and score becomes 1.
There is no need to play the 1st token since you cannot play it face up to add to your score.
Example 3:

Input: tokens = [100,200,300,400], power = 200
Output: 2
Explanation: Play the tokens in this order to get a score of 2:
1. Play the 0th token (100) face up, your power becomes 100 and score becomes 1.
2. Play the 3rd token (400) face down, your power becomes 500 and score becomes 0.
3. Play the 1st token (200) face up, your power becomes 300 and score becomes 1.
4. Play the 2nd token (300) face up, your power becomes 0 and score becomes 2.


Constraints:

0 <= tokens.length <= 1000
0 <= tokens[i], power < 104

Question link https://leetcode.com/problems/bag-of-tokens/
"""
from typing import List


class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        score = 0
        tokens.sort()
        i, j = 0, len(tokens) - 1
        mx = 0
        while i <= j:
            if tokens[i] <= power:
                power -= tokens[i]
                score += 1
                i += 1
                mx = max(mx, score)
            elif score > 0:
                score -= 1
                power += tokens[j]
                j -= 1
            else:
                break
        return mx


# Input: tokens = [100,200,300,400], power = 200 score = 0

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        i, j = 0, len(tokens)
        score = 0
        tsort = sorted(tokens)
        while i < j:
            if power >= tsort[i]:
                power -= tsort[i]
                score += 1
                i += 1
            else:
                if i + 1 < j and score > 0:
                    power += tsort[j - 1]
                    j -= 1
                    score -= 1
                else:
                    break
        return score


x = Solution()
print(x.bagOfTokensScore([100, 200, 300, 400], 200))
