def leftMost(s):
    m = {}
    res = -1
    for i in range(len(s)-1, -1, -1):
        if s[i] in m:
            res = i
        else:
            m[s[i]] = i
    return res

print(leftMost('abba'))
