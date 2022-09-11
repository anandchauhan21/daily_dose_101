"""
maximum-performance-of-a-team
You are given two integers n and k and two integer arrays speed and efficiency both of length n. There are n engineers numbered from 1 to n. speed[i] and efficiency[i] represent the speed and efficiency of the ith engineer respectively.
Choose at most k different engineers out of the n engineers to form a team with the maximum performance.
The performance of a team is the sum of their engineers' speeds multiplied by the minimum efficiency among their engineers.
Return the maximum performance of this team. Since the answer can be a huge number, return it modulo 109 + 7.

Example 1:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
Output: 60
Explanation:
We have the maximum performance of the team by selecting engineer 2 (with speed=10 and efficiency=4) and engineer 5 (with speed=5 and efficiency=7). That is, performance = (10 + 5) * min(4, 7) = 60.

Example 2:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
Output: 68
Explanation:
This is the same example as the first but k = 3. We can select engineer 1, engineer 2 and engineer 5 to get the maximum performance of the team. That is, performance = (2 + 10 + 5) * min(5, 4, 7) = 68.

Example 3:
Input: n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
Output: 72

Constraints:
1 <= k <= n <= 105
speed.length == n
efficiency.length == n
1 <= speed[i] <= 105
1 <= efficiency[i] <= 108

Question link https://leetcode.com/problems/maximum-performance-of-a-team/
"""
import heapq
from typing import List


class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        eng = zip(efficiency, speed)
        eng = sorted(eng, key=lambda x: x[0], reverse=True)
        sumSpeed, res = 0, 0
        speedHeap = []
        for e, s in eng:
            heapq.heappush(speedHeap, s)
            sumSpeed += s
            if len(speedHeap) > k:
                sumSpeed -= heapq.heappop(speedHeap)

            res = max(res, sumSpeed * e)
        return res % (10 ** 9 + 7)


x = Solution()
print(x.maxPerformance(6, [2, 10, 3, 1, 5, 8], [5, 4, 3, 9, 7, 2], 2))