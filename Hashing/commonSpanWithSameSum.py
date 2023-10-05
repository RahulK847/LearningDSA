#Longest common span with same sum in binary arrays
# naive SOl
def maxi(arr1, arr2):
    res = 0
    for i in range(len(arr1)):
        sum1, sum2 = 0, 0
        for j in range(i, len(arr1)):
            sum1 += arr1[j]
            sum2 += arr2[j]
            if sum1 == sum2:
                res = max(res, j - i + 1)
    return res
def maxj(arr1, arr2):
    n = len(arr1)
    myDict = dict()
    sum = 0
    maxlen = 0
    for i in range(n):
        sum += arr1[i]-arr2[i]
        if sum == 0:
            maxlen = i + 1
        elif sum in myDict:
            maxlen = max(maxlen, i - myDict[sum])
        if sum not in myDict:
            myDict[sum] = i
    return maxlen


arr1 = [1,0,0, 0, 1]
arr2 = [1,1,1 , 1, 1]
print(maxj(arr1, arr2))
