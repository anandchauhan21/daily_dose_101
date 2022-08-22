'''
def bs(lst, i):
    l, r = 0, len(lst)
    print(type(l))
    while l < r:
        mid = (l + r) // 2
        if i < lst[mid]:
            r = [mid]
        else:
            l = mid + 1
    return l


x = bs(["a", "bb", "acd"], 1)

'''


# Function to calculate distance
from collections import Counter


def resistance(r1, r2):
    return (r1 * r2) / (r1 + r2)


print(resistance(3, 4))


def starno(n):
    for i in range(n):
        out = 6 * i * (i - 1) + 1
        print(out)
x = starno(10)
n = 10
def size(n):
    x = 36*16/n
    return x
print(size(n))

D = dict()#no,name,city,gende




sd = [[1,'raj','bhopal','m'],[2,'jay','rajsathan','m'],[3,'om','bhopal','m']]
print(sd[1][2])
n = len(sd)

def city(n):
    cc = {}
    for i in range(n):
        if sd[i][2] not in cc:
            cc[sd[i][2]] = 1
        else:
            cc[sd[i][2]] +=1
    print(cc)

x = city(n)
