from typing import List


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        def check(num):
            mask = 1 << (8-1)
            i = 0
            while num & mask:
                mask >>= 1
                i += 1
            return i
        i = 0
        while i < len(data):
            j = check(data[i])
            k = i+j-(j!=0)
            i += 1
            if j == 1 or j > 4 or k >= len(data): return False
            while i < len(data) and i <= k:
                cur = check(data[i])
                if cur != 1: return False
                i += 1
        return True

x = Solution()
print(x.validUtf8([197,130,1]))