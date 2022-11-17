"""
rectangle-area
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

Example 1:

Rectangle Area
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45
Example 2:

Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16


Constraints:

-104 <= ax1 <= ax2 <= 104
-104 <= ay1 <= ay2 <= 104
-104 <= bx1 <= bx2 <= 104
-104 <= by1 <= by2 <= 104

Question link https://leetcode.com/problems/rectangle-area/
"""


class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        area_a = (ax2 - ax1) * (ay2 - ay1)
        area_b = (bx2 - bx1) * (by2 - by1)

        # x overlap
        xtop = min(ax2, bx2)
        xbot = max(ax1, bx1)
        x_over = xtop - xbot

        # y overlap
        ytop = min(ay2, by2)
        ybot = max(ay1, by1)
        y_over = ytop - ybot

        over_area = 0

        if x_over > 0 and y_over > 0:
            over_area = x_over * y_over

        # overlap_area = ((min(ax2, bx2) - max(ax1, bx1)) * (min(ay2, by2) - max(ay1, by1)))
        x = area_a + area_b - over_area
        return x

x = Solution()
print(x.computeArea(-3,
0,
3,
4,
0,
-1,
9,
2))