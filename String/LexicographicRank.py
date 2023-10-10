# Lexicographic Rank of a String
def fact(n):
    if n <= 1:
        return 1
    return n * fact(n - 1)

def findRank(s):
    n = len(s)
    rank = 1
    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if s[i] > s[j]:
                count += 1
        rank += count * fact(n - i - 1)
    return rank


s = "string"
print(findRank(s))


