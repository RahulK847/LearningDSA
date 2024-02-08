def NextGreaterElement(arr):
    if not arr:
        return []

    res = [-1]
    stack = [arr[-1]]
    for i in arr[-2::-1]:
        while stack != [] and stack[-1] <= i:
            stack.pop()
        if not stack:
            stack.append(i)
            res.append(-1)
        else:
            res.append(stack[-1])
            stack.append(i)
    return res[::-1]

print(NextGreaterElement([5, 15, 8, 6, 12, 9, 18]))
