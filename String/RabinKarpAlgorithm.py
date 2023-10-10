# Rabin Karp Algorithm
def RKSearch(pattern, txt):
    j, p, t, h, q, d, n, m = 0, 0, 0, 1, 101, 10, len(txt), len(pattern)
    # The variable H is need to remove 1st element of curr window so that we can add next element
    for i in range(m - 1):
        h = (h * d) % q
    # Calculate the hash value for pattern and text
    for i in range(m):
        p = (p * d + ord(pattern[i])) % q
        t = (t * d + ord(txt[i])) % q
    # Find the match by slide the pattern over text one by one
    for i in range(n - m + 1):
        if p == t:
            for j in range(m):
                if txt[i + j] != pattern[j]:
                    break
            if j == m - 1:
                print("Pattern is found at position: " + str(i))
        if i < n - m:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + m])) % q

            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t += q


txt = "GEEKS FOR GEEKS"
pattern = "GEEK"
RKSearch(pattern, txt)
