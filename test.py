from collections import defaultdict
from typing import List

paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)",
         "root/c/d 4.txt(efgh)","root 4.txt(efgh)"]
class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        c = defaultdict(list)
        for path in paths:
            path = path.split()
            root = path[0]
            for f in path[1:]:
                file_name,_,content = f.partition("(")
                c[content].append(root+'/'+file_name)
        return [x for x in c.values() if len(x) >1]


x = Solution()
print(x.findDuplicate(["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"]))



