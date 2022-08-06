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