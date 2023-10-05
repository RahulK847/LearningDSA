def lenOfLongSubarr(arr):
    n = len(arr)
    myDict = dict()
    sum = 0
    maxlen = 0
    for i in range(n):
        if arr[i]==0:
            arr[i] = -1
        sum += arr[i]
        if sum == 0:
            maxlen = i+1
        elif sum in myDict:
            maxlen = max(maxlen, i - myDict[sum])
        if sum not in myDict:
            myDict[sum] = i
    return maxlen


arr = [0,1,1,1,0,1,0,0]
print(lenOfLongSubarr(arr))