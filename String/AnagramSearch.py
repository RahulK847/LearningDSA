# Anagram Search
def isAnagramPresent(txt , pat):
    txt_hash = {}
    pat_hash = {}
    p = len(pat)
    for i in range(p):
        txt_hash[txt[i]] = 1 + txt_hash.get(txt[i], 0)
        pat_hash[pat[i]] = 1 + pat_hash.get(pat[i], 0)

    res = [0] if pat_hash == txt_hash else []

    for i in range(p, len(txt)):
        if txt_hash[txt[i-p]] == 1:
            txt_hash.pop(txt[i-p])
        else:
            txt_hash[txt[i - p]] -= 1
        txt_hash[txt[i]] = 1 + txt_hash.get(txt[i], 0)
        if txt_hash == pat_hash:
            res.append(i-p+1)
    return res



print(isAnagramPresent("geeksforgeeks", "geek"))