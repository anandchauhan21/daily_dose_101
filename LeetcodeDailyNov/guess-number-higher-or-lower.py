"""
guess-number-higher-or-lower
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.



Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1


Constraints:

1 <= n <= 231 - 1
1 <= pick <= n

Question link https://leetcode.com/problems/guess-number-higher-or-lower/
"""


def guess(mid):
    pass


class Solution:
    def guessNumber(self, n: int) -> int:
        low  = 1 
        high = n
        while low <= high:
            mid = low + (high - low) // 2
            res = guess(mid)
            if res == 0:
                return mid
            elif res < 0:
                high = mid - 1
            else:
                low = mid + 1