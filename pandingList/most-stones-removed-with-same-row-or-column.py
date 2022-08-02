"""
most-stones-removed-with-same-row-or-column

On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most one stone.

A stone can be removed if it shares either the same row or the same column as another stone that has not been removed.

Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone, return the largest possible number of stones that can be removed.



Example 1:

Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5
Explanation: One way to remove 5 stones is as follows:
1. Remove stone [2,2] because it shares the same row as [2,1].
2. Remove stone [2,1] because it shares the same column as [0,1].
3. Remove stone [1,2] because it shares the same row as [1,0].
4. Remove stone [1,0] because it shares the same column as [0,0].
5. Remove stone [0,1] because it shares the same row as [0,0].
Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
Example 2:

Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3
Explanation: One way to make 3 moves is as follows:
1. Remove stone [2,2] because it shares the same row as [2,0].
2. Remove stone [2,0] because it shares the same column as [0,0].
3. Remove stone [0,2] because it shares the same row as [0,0].
Stones [0,0] and [1,1] cannot be removed since they do not share a row/column with another stone still on the plane.
Example 3:

Input: stones = [[0,0]]
Output: 0
Explanation: [0,0] is the only stone on the plane, so you cannot remove it.


Constraints:

1 <= stones.length <= 1000
0 <= xi, yi <= 104
No two stones are at the same coordinate point.

Question link https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
"""
from collections import defaultdict, deque
from typing import List


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        # create a completed graph, use graphX to store the node with same x axis and use graphY to store  the node with the same y axis
        # Use BFS
        # Use visited to store the passed node
        # for one conneted graph count the (node number -1), and let it be ni
        # At the end, add all the ni in each connected graphs
        # Time: O(V+E) Space:O(V+E)

        hmapX = defaultdict(list)
        hmapY = defaultdict(list)
        for st in stones:
            hmapX[st[0]].append(tuple(st))
            hmapY[st[1]].append(tuple(st))

        visited = set()

        count = 0
        for st in stones:
            if tuple(st) not in visited:
                queue = deque([tuple(st)])
                while queue:
                    curr = queue.popleft()
                    count += 1
                    visited.add(curr)
                    for nei in hmapX[curr[0]]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
                    for nei in hmapY[curr[1]]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
                count -= 1
        return count