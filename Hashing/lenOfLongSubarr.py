def lenOfLongSubarr(arr, k):
    n = len(arr)
    myDict = dict()
    sum = 0
    maxlen = 0
    for i in range(n):
        sum += arr[i]
        if sum == k:
            maxlen = i+1
        elif sum-k in myDict:
            maxlen = max(maxlen, i - myDict[sum-k])
        if sum not in myDict:
            myDict[sum] = i
    return maxlen


arr = [1,2,1,2,1]
print(lenOfLongSubarr(arr, 3))