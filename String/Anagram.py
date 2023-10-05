#Check For Anagram
from collections import defaultdict
def isAnagram(s, t):
        count = defaultdict(int)
        for i in s:
            count[i]+=1
        for i in t:
            count[i]-=1
        for val in count.values():
            if val !=0:
                return False
        return True

print(isAnagram("listen", "silent"))