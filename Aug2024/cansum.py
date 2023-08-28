# time complexity is 0(n**m) and space complexity is 0(m)
def canSum(target,numbers):
    if target ==0:return True;
    if target <0:return False;
    for num in numbers:
        reminder = target - num
        if canSum(reminder,numbers) == True:return True
    return False
#print(canSum(8,[2,3,5]))
cash = {}
def canSumNew(target,numbers,cash):
    if target in cash:return cash[target];
    if target ==0:return True;
    if target <0:return False;
    for num in numbers:
        reminder = target - num
        if canSum(reminder,numbers,cash) == True:
            cash[target] = True
            return True
    cash[target] = False
    return False
#print(canSum(300,[7,14]))


def has_pair_with_sum(arr, target):
    num_dict = {}  # Dictionary to store numbers and their indices

    for i, num in enumerate(arr):
        complement = target - num

        if complement in num_dict:
            return True  # Found a pair that adds up to the target

        num_dict[num] = i  # Store the number in the dictionary

    return False  # No pair found


# Example usage
arr = [2,3]
target = 7
result = has_pair_with_sum(arr, target)
print(result)  # Output will be True because 2 + 7 = 9

