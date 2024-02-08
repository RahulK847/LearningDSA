def PrevGreaterElement(arr):
    if not arr:
        return []

    res = [-1]
    stack = [arr[0]]
    for i in arr[1:]:
        while stack != [] and stack[-1] <= i:
            stack.pop()
        if not stack:
            stack.append(i)
            res.append(-1)
        else:
            res.append(stack[-1])
            stack.append(i)
    return res


arr = [18, 9, 12, 6, 8, 10, 15, 5]
print(PrevGreaterElement(arr))
