#Count Distinct Elements In Every Window
def printDistinct(arr, k):
    n = len(arr)
    for i in range(n-k+1):
        count = 0
        for j in range(k):
            flag = False
            for p in range(j):
                if arr[i+j] == arr[i+p]:
                    flag = True
                    break
            if flag == False:
                count+=1
        print(count, end=" ")

def printDistinct2(arr, k):
    tempDict = dict()
    n = len(arr)
    for i in range(k):
        if arr[i] in tempDict:
            tempDict[arr[i]]+=1
        else:
            tempDict[arr[i]] = 1
    print(len(tempDict), end=" ")
    for i in range(k, n):
        if tempDict[arr[i-k]] - 1 <= 0:
            tempDict.pop(arr[i-k])
        else:
            tempDict[arr[i-k]] -= 1
        if arr[i] in tempDict:
            tempDict[arr[i]] += 1
        else:
            tempDict[arr[i]] = 1
        print(len(tempDict), end=" ")

printDistinct2([1,2,2,1,3,4,1], 4)







