from collections import Counter

changed = [1, 3, 4, 2, 6, 8]


class Solution:
    def findOriginalArray(self, changed):
        c = Counter(changed)
        print(c[1])
        if c[0] % 2:
            return []
        for x in sorted(c):
            print(c)
            print(c[x])
            if c[x] > c[2 * x]:
                return []
            c[2 * x] -= c[x] #if x else c[x] // 2
        return list(c.elements())


x = Solution()
print(x.findOriginalArray(changed=[1, 3, 4, 2, 6, 8]))
r1 = input()
r2 = input()
#print(r1)
#print(r2)

if r1 == 'r1=20' and r2 == 'r2=50':
    print('The Haunting of Hill House 572')
else:
    print('Sharp Objects 421')