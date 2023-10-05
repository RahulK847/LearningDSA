# Subarray with Zero Sum
def ZeroSumSubarr(arr):
    pre_sum = 0
    num_Set = set()
    for i in arr:
        pre_sum += i
        if pre_sum == 0 or pre_sum in num_Set:
            return True
        num_Set.add(pre_sum)
    return False


print(ZeroSumSubarr([1, 4, 13, -3, -10, 5]))
