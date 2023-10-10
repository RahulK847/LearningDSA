# KMP(Knuth-Morris-Pratt) algorithm
def fillLPS(pat, m, lps):
    prevLPS, i = 0, 1
    while i < m:
        if pat[i] == pat[prevLPS]:
            lps[i] = prevLPS + 1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS - 1]


def KMPSearch(pat, txt):
    m, n = len(pat), len(txt)
    # Create and compute the LPS array
    lps = [0] * m
    fillLPS(pat, m, lps)
    i = 0  # ptr for text
    j = 0  # ptr for pat
    while i < n:
        if pat[j] == txt[i]:
            i, j = i + 1, j + 1
        if j == m:
            print("Pattern is found at position: " + str(i - j))
            j = lps[j - 1]
        elif i < n and pat[j] != txt[i]:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]



txt = "GEEKS FOR GEEKS"
pattern = "GEEK"
KMPSearch(pattern, txt)
