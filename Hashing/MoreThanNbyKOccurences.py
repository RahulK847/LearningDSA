# def printNByK(arr, k):
#     n = len(arr)
#     target = n // k
#     numDict = dict()
#     for i in arr:
#         if i in numDict:
#             numDict[i]+=1
#             if numDict[i]>target:
#                 print(i, end=" ")
#         else:
#             numDict[i] = 1
#
# printNByK([30, 10, 20, 20, 10, 20, 30, 30], 4)
#
m = {
    1:0,
    2:3
}
for i, j in m.items():
    print(i+j)