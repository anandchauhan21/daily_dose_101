"""
candy
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.
You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.

Example 1:
Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:
Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Constraints:
n == ratings.length
1 <= n <= 2 * 104
0 <= ratings[i] <= 2 * 104

Question link https://leetcode.com/problems/candy/
"""

from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        N = len(ratings)
        o = [1 for _ in range(N)]
        for i in range(1,N):
            if ratings[i] > ratings[i-1]:
                o[i] = max(o[i-1]+1, o[i])
        for i in range(N-2,-1,-1):
            if ratings[i] > ratings[i+1]:
                o[i] = max(o[i+1]+1,o[i])
        return sum(o)

x = Solution()
print(x.candy([1,0,2]))