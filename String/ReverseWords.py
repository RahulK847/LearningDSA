#Reverse words in a string
def reverseWords(s):
    s = list(s)
    n = len(s)
    start = 0
    for i in range(n):
        if s[i] == " ":
            reverse(s, start, i - 1)
            start = i + 1
    reverse(s, start, n - 1)
    reverse(s, 0, n - 1)
    return ''.join(s)


def reverse(s, low, high):
    while low <= high:
        s[low], s[high] = s[high], s[low]
        low += 1
        high -= 1

a = "hello world"
print(a)
print(reverseWords(a))
