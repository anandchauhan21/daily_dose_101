"""
Write a function *howSum(targetSum, numbers)* that takes in a
array of numbers as arguments.

The function should return an array containing any combination of
elements that add up to exactly the targetSum. If there is no
combination that adds up to the targetSum, then return null.

If there are multiple combinations possible, you may return any
single one.


nums = [5,3,4,7]
tr = 7

def howSum(tr, nums):

    for num in nums:
        if tr == 0: return []
        if tr < 0: return None
        reminder = tr - num
        print(f"tr = {tr}, num = {num}, reminder = {reminder}")

        rr = howSum(reminder,nums)
        #print(rr)
        if reminder != None:
            return rr.append(num)
    return None
print(howSum(tr,nums))
"""


def find_target_elements(target, num_list):
    seen = {}  # A dictionary to store seen elements and their indices

    for idx, num in enumerate(num_list):
        complement = target - num
        print(f"tr = {target}, num = {num}, reminder = {complement}")
        print(f"Seen {seen}")
        if complement in seen:
            return [num, complement]

        seen[num] = idx

    return None


target = 7
num_list = [2,3]
result = find_target_elements(target, num_list)
print(result)  # Output: [3, 4]
