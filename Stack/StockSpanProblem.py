# stock Span Problem
# I/P = [13, 15, 12, 14, 16, 8, 6, 4, 10, 30]      [10, 20, 30, 40]      [40, 30, 20, 10]
# o/p = [ 1,  2,  1,  2,  5, 1, 1, 1,  4, 10]      [ 1,  2,  3,  4]      [ 1,  1,  1,  1]


def naive_sol(arr):
    n = len(arr)

    for i in range(n):
        span = 1
        for j in range(i - 1, -1, -1):
            if arr[i] >= arr[j]:
                span += 1
            else:
                break
        print(span, end=" ")


def calculateSpan(arr):
    stack = []
    stack.append(0)
    print(1, end=" ")
    for i in range(1, len(arr)):
        while stack != [] and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if not stack:
            print(i + 1, end=" ")
        else:
            print(i - stack[-1], end=" ")
        stack.append(i)


calculateSpan([10, 20, 30, 40])
