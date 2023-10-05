def MostRepeatedLetter(s):
    charDict = {}
    res = s[0]
    count = 1
    for i in s:
        if i in charDict:
            charDict[i]+=1
            if count<charDict[i]:
                res = i
                count = charDict[i]
            if count == charDict[i]:
                res = min(i, res)
        else:
            charDict[i] = 1
            if count == charDict[i]:
                res = min(i, res)
    return res

print(MostRepeatedLetter('qwerty'))
