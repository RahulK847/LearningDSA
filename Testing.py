def aaaa(p, s):
    d = {}
    s = list(s.split())
    for i in range(len(p)):
        if s[i] in d:
            if d[s[i]] != p[i]:
                return False
        else:
            d[s[i]] = p[i]
        if p[i] in d:
            if d[p[i]] != s[i]:
                return False
        else:
            d[p[i]] = s[i]
    return True


print(aaaa("abba", "dog cat cat fish"))