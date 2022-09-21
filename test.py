from typing import List


# Input: nums = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evnesum = sum(i for i in nums if i % 2 == 0)
        for i in range(len(queries)):
            val, id = queries[i]
            if nums[id] % 2 == 0: evnesum -= nums[id]
            nums[id] += val
            if nums[id] % 2 == 0: evnesum += nums[id]
            queries[i] = evnesum
        return queries


x = Solution()
print(x.sumEvenAfterQueries([1, 2, 3, 4], [[1, 0], [-3, 1], [-4, 0], [2, 3]]))
