def givenSum(arr, sum):
    h = set()
    prefix_sum = 0
    for i in arr:
        prefix_sum += i
        h.add(prefix_sum)
        if (prefix_sum-sum) in h:
            return True
            break
    return False


arr = [5, 8, 6, 13, 3, -1]
sum = 22
print(givenSum(arr, sum))