def isSubSeq(s1, s2):
    i, j = 0, 0
    while i < len(s1):
        if s1[i] == s2[j]:
            i += 1
            j += 1
        else:
            i += 1
    return (j==len(s2))

def isSubSeqRecu(s1, s2, n, m):
    if m==0:
        return True
    if n==0:
        return False
    if s1[n-1] == s2[m-1]:
        return isSubSeqRecu(s1, s2, n-1, m-1)
    else:
        return isSubSeqRecu(s1, s2, n-1, m)


s1 = 'abcd'
s2 = 'ad'
print(isSubSeqRecu(s1, s2, len(s1), len(s2)))
