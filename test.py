from typing import List
# nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# output: 3

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        nums2_str = "".join([chr(i) for i in nums2])
        max_str = ""
        res = 0
        for i in nums1:
            max_str += chr(i)
            if max_str in nums2_str:
                res = max(res,len(max_str))
            else:
                max_str = max_str[1:]
        return res




x = Solution()
print(x.findLength(nums1=[1, 2, 3, 2, 1], nums2=[3, 2, 1, 4, 7]))