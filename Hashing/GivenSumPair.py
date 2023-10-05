def givenSum(arr, sum):
    h = set()
    for i in arr:
        if (sum-i) in h:
            return True
        else:
            h.add(i)
    return False

arr = [8, 3, 4, 2, 5]
print(givenSum(arr, 6))
